"""Check local README images and hand-authored SVGs without network access."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class ImageReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "img" and attrs.get("src"):
            self.paths.append(attrs["src"])
        if tag in {"img", "source"} and attrs.get("srcset"):
            self.paths.extend(item.strip().split()[0]
                              for item in attrs["srcset"].split(",") if item.strip())


def main():
    try:
        readme = (ROOT / "README.md").read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as error:
        print(f"Cannot read README.md: {error}", file=sys.stderr)
        return 1
    parser = ImageReferences()
    parser.feed(readme)
    markdown_paths = re.findall(
        r'!\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+"[^"\n]*")?\s*\)', readme
    )
    paths = parser.paths + [angled or plain for angled, plain in markdown_paths]
    errors = []
    checked = set()
    # Preserve source order while reporting each repeated reference only once.
    for reference in dict.fromkeys(paths):
        try:
            url = urlsplit(reference)
        except ValueError as error:
            errors.append(f"Invalid image URL {reference}: {error}")
            continue
        if url.scheme or url.netloc or not url.path:
            continue
        path = (ROOT / unquote(url.path)).resolve()
        if not path.is_relative_to(ROOT):
            errors.append(f"Image escapes repository: {reference}")
        elif not path.is_file():
            errors.append(f"Missing image: {reference}")
        checked.add(reference)

    svgs = sorted(
        path for path in (ROOT / "assets").rglob("*")
        if path.is_file() and path.suffix.lower() == ".svg"
    )
    for path in svgs:
        try:
            element = ET.parse(path).getroot()
            if element.tag != "{http://www.w3.org/2000/svg}svg":
                errors.append(f"Invalid SVG root: {path.relative_to(ROOT)}")
        except OSError as error:
            errors.append(f"Cannot read SVG {path.relative_to(ROOT)}: {error}")
        except ET.ParseError as error:
            errors.append(f"Malformed SVG {path.relative_to(ROOT)}: {error}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"OK: {len(checked)} local image references and {len(svgs)} SVGs checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
