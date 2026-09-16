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


if __name__ == "__main__":
    unittest.main()
