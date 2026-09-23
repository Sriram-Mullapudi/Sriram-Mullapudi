"""Regression checks for recursive profile SVG validation."""

from contextlib import redirect_stderr, redirect_stdout
import importlib.util
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_profile.py"
spec = importlib.util.spec_from_file_location("check_profile", SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class NestedSvgTests(unittest.TestCase):
    def check_svg(self, contents):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("# Profile\n", encoding="utf-8")
            nested = root / "assets" / "icons"
            nested.mkdir(parents=True)
            (nested / "sample.svg").write_text(contents, encoding="utf-8")
            output, errors = StringIO(), StringIO()
            with patch.object(checker, "ROOT", root), redirect_stdout(output), redirect_stderr(errors):
                result = checker.main()
            return result, output.getvalue(), errors.getvalue()

    def test_nested_malformed_svg_is_rejected(self):
        result, _, errors = self.check_svg("<svg>")
        self.assertEqual(result, 1)
        self.assertIn("Malformed SVG", errors)
        self.assertIn("sample.svg", errors)

    def test_nested_valid_svg_is_counted(self):
        result, output, errors = self.check_svg('<svg xmlns="http://www.w3.org/2000/svg"/>')
        self.assertEqual(result, 0)
        self.assertIn("1 SVGs checked", output)
        self.assertEqual(errors, "")


class FileReadTests(unittest.TestCase):
    def test_missing_readme_reports_error_without_traceback(self):
        with TemporaryDirectory() as directory:
            errors = StringIO()
            with patch.object(checker, "ROOT", Path(directory)), redirect_stderr(errors):
                result = checker.main()
            self.assertEqual(result, 1)
            self.assertIn("Cannot read README.md:", errors.getvalue())

    def test_unreadable_svg_reports_error_without_traceback(self):
        with patch.object(checker.ET, "parse", side_effect=PermissionError("access denied")):
            result, _, errors = NestedSvgTests().check_svg('<svg xmlns="http://www.w3.org/2000/svg"/>')
        self.assertEqual(result, 1)
        self.assertIn("Cannot read SVG", errors)
        self.assertIn("access denied", errors)


class RepeatedImageTests(unittest.TestCase):
    def test_duplicate_markdown_and_html_images_report_once(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                '![First](assets/missing.png)\n'
                '<img src="assets/missing.png">\n'
                '<source srcset="assets/missing.png 1x, assets/other.png 2x">',
                encoding="utf-8",
            )
            errors = StringIO()
            with patch.object(checker, "ROOT", root), redirect_stderr(errors):
                result = checker.main()
            self.assertEqual(result, 1)
            self.assertEqual(errors.getvalue().splitlines(), [
                "Missing image: assets/missing.png",
                "Missing image: assets/other.png",
            ])


class ImageSyntaxTests(unittest.TestCase):
    def run_readme(self, readme, files=None):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(readme, encoding="utf-8")
            for name, content in (files or {}).items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            output, errors = StringIO(), StringIO()
            with patch.object(checker, "ROOT", root), redirect_stdout(output), redirect_stderr(errors):
                result = checker.main()
            return result, output.getvalue(), errors.getvalue()

    def test_invalid_url_does_not_stop_remaining_checks(self):
        result, _, errors = self.run_readme(
            '<img src="https://[broken/image.png"><img src="assets/missing.png">'
        )
        self.assertEqual(result, 1)
        self.assertIn("Invalid image URL", errors)
        self.assertIn("Missing image: assets/missing.png", errors)


    def test_angle_bracket_image_path_with_spaces_and_title(self):
        result, output, errors = self.run_readme(
            '![Preview](<assets/my image.png> "Profile preview")',
            {"assets/my image.png": "placeholder"},
        )
        self.assertEqual(result, 0)
        self.assertIn("1 local image references", output)
        self.assertEqual(errors, "")

    def test_missing_angle_bracket_image_is_reported(self):
        result, _, errors = self.run_readme('![Preview](<assets/missing image.png>)')
        self.assertEqual(result, 1)
        self.assertIn("Missing image: assets/missing image.png", errors)


    def test_uppercase_svg_extension_is_validated(self):
        result, _, errors = self.run_readme(
            "# Profile", {"assets/icons/BROKEN.SVG": "<svg>"}
        )
        self.assertEqual(result, 1)
        self.assertIn("Malformed SVG", errors)
        self.assertIn("BROKEN.SVG", errors)

    def test_svg_named_directory_is_not_parsed(self):
        result, output, errors = self.run_readme(
            "# Profile", {"assets/folder.svg/readme.txt": "notes"}
        )
        self.assertEqual(result, 0)
        self.assertIn("0 SVGs checked", output)
        self.assertEqual(errors, "")


    def test_missing_accessibility_label_is_reported(self):
        svg = '<svg xmlns="http://www.w3.org/2000/svg" aria-labelledby="missing"/>'
        result, _, errors = self.run_readme("# Profile", {"assets/icon.svg": svg})
        self.assertEqual(result, 1)
        self.assertIn("Broken aria-labelledby reference 'missing'", errors)

    def test_valid_multiple_accessibility_references_pass(self):
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" aria-labelledby="title subtitle" '
               'aria-describedby="description"><title id="title">Title</title>'
               '<text id="subtitle">Subtitle</text><desc id="description">Description</desc></svg>')
        result, _, errors = self.run_readme("# Profile", {"assets/icon.svg": svg})
        self.assertEqual(result, 0)
        self.assertEqual(errors, "")

    def test_nested_missing_description_is_reported(self):
        svg = ('<svg xmlns="http://www.w3.org/2000/svg">'
               '<g aria-describedby="missing"/></svg>')
        result, _, errors = self.run_readme("# Profile", {"assets/icon.svg": svg})
        self.assertEqual(result, 1)
        self.assertIn("Broken aria-describedby reference 'missing'", errors)


    def test_duplicate_svg_ids_are_reported_once(self):
        svg = ('<svg xmlns="http://www.w3.org/2000/svg">'
               '<title id="label">Title</title><g id="label"><path id="label"/></g></svg>')
        result, _, errors = self.run_readme("# Profile", {"assets/icon.svg": svg})
        self.assertEqual(result, 1)
        self.assertEqual(errors.count("Duplicate SVG id 'label'"), 1)

    def test_svg_ids_can_repeat_across_separate_files(self):
        svg = '<svg xmlns="http://www.w3.org/2000/svg"><title id="title">Title</title></svg>'
        result, _, errors = self.run_readme(
            "# Profile", {"assets/one.svg": svg, "assets/two.svg": svg}
        )
        self.assertEqual(result, 0)
        self.assertEqual(errors, "")


    def test_missing_local_svg_href_is_reported(self):
        svg = '<svg xmlns="http://www.w3.org/2000/svg"><use href="#missing"/></svg>'
        result, _, errors = self.run_readme("# Profile", {"assets/icon.svg": svg})
        self.assertEqual(result, 1)
        self.assertIn("Broken SVG href '#missing'", errors)

    def test_missing_legacy_svg_href_is_reported(self):
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" '
               'xmlns:xlink="http://www.w3.org/1999/xlink"><use xlink:href="#missing"/></svg>')
        result, _, errors = self.run_readme("# Profile", {"assets/icon.svg": svg})
        self.assertEqual(result, 1)
        self.assertIn("Broken SVG href '#missing'", errors)

    def test_svg_forward_and_external_references_pass(self):
        svg = ('<svg xmlns="http://www.w3.org/2000/svg">'
               '<use href="#sh%61pe"/><path id="shape"/>'
               '<use href="other.svg#symbol"/><a href="https://example.com/#about"/></svg>')
        result, _, errors = self.run_readme("# Profile", {"assets/icon.svg": svg})
        self.assertEqual(result, 0)
        self.assertEqual(errors, "")


if __name__ == "__main__":
    unittest.main()
