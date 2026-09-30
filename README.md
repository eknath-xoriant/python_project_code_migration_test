# Python 3.7 Migration Test Repo

Small Python 3.7-compatible codebase meant to surface common migration edits when moving to Python 3.11.

## Files
- `main.py` — CLI entry point and basic processing flow
- `data_models.py` — dataclasses and type hints
- `legacy_utils.py` — intentionally legacy patterns to update during migration

## Run
```bash
python main.py --name "Ada" --count 3
```
