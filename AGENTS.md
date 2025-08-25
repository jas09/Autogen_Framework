# Project Ops Hints for Codex

## Python env
- Use Python 3.10+ and `pip`.
- Install dev deps with:
  pip install -r requirements.txt
  pip install pytest pytest-cov

## Tests
- Run tests with:
  pytest -q

## Playwright (Python)
- If missing:
  pip install playwright pytest-playwright
  playwright install --with-deps
- Tests live in tests/e2e/
- Use pytest style with fixtures & parametrization.

## CI
- GitHub Actions workflows in .github/workflows/*.yml
- Preferred fixes: smallest change, clear commit message, link to failing job.
