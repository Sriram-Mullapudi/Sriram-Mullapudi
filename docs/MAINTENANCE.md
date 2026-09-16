# Maintaining this GitHub profile

This repository powers the README shown on the `Sriram-Mullapudi` GitHub profile.

## Where to make changes

| Content | Source |
| --- | --- |
| Introduction, projects, experience, and full skills list | `README.md` |
| Profile banner | `assets/engineering-banner.svg` |
| Six linked skill panels | `assets/skill-*.svg` |
| Contribution snake generation | `.github/workflows/snake.yml` |
| Activity summary generation | `.github/workflows/profile-summary-cards.yml` |

The README determines which assets appear on the profile. An asset remaining in
`assets/` does not necessarily mean it is currently displayed.

## Updating skills and project evidence

1. Edit the relevant panel and the expandable text skills list together.
2. Keep SVG titles, descriptions, and README image alternatives meaningful.
3. Preserve the distinction between real-world usage and controlled test results.
4. Check each panel's destination link after changing a project URL.
5. Preview the README on GitHub at desktop and narrow mobile widths. Confirm that
   the panels wrap, text remains readable, and the full skills list opens.

Keep important information available as Markdown text; the SVG panels supplement
it. Avoid adding credentials, personal access tokens, or private project data.

## How the animations stay current

The snake workflow runs every 12 hours, on pushes to `main`, and through manual
workflow dispatch. It publishes light and dark SVGs to the `output` branch.
The README selects the matching asset through a `<picture>` element.

To investigate a stale snake, check the latest **Generate Contribution Snake** run
in GitHub Actions before changing the README links. Generated files on `output`
are replaced by the next successful run; make durable changes in the workflow.

The profile summary workflow runs daily and can also be dispatched manually.
It uses the configured `SUMMARY_GITHUB_TOKEN` secret. If it fails, check the run
logs and secret configuration without copying the secret into a file or issue.

## Before publishing

- Run `git diff --check` and review the staged diff.
- Check that referenced local images exist and linked public pages open.
- Confirm that metrics, employment dates, and contact details are accurate.
- Commit on `main` and push normally; do not force-push profile history.
- Open the public profile to confirm the new README and assets are visible.

## Cross-platform editing

`.gitattributes` keeps Markdown, SVG, and workflow files on LF line endings across
Windows and Linux, while preserving raster images as binary files. This avoids
line-ending-only diffs when editing locally or regenerating assets in Actions.

EditorConfig-aware editors also use `.editorconfig` for UTF-8, LF line endings,
final newlines, and two-space YAML/SVG indentation. Markdown trailing spaces are
preserved because they can represent intentional line breaks.

## Local preview files

Use `.preview/` for temporary screenshots or rendered README previews. It is
ignored along with operating-system metadata and Python bytecode caches.
Keep published images in `assets/`; generated activity cards remain tracked in
`profile-summary-card-output/`.

## Check profile assets locally

Run `python scripts/check_profile.py` from the repository root with Python 3.9+
before publishing image changes. The check reports missing local README images,
paths outside the repository, and malformed SVGs in `assets/`. It exits with a
nonzero status when a problem is found and requires no third-party packages.

This is an offline asset check, not a visual preview or an external-link check.
Continue to inspect the rendered profile on desktop and mobile.

The asset check includes SVGs in nested `assets/` folders. Run its regression
checks with `python -m unittest discover -s tests` before modifying the checker.
