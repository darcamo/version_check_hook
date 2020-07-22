# version_check_hook

A pre-commit hook that checks the version in `pyproject.toml` is the same as in a `__init__.py` file

Add this to you `.pre-commit-config.yaml` file

```yaml
repos:
- repo: https://github.com/darcamo/version_check_hook.git
  rev: v1.1
  hooks:
  - id: version_check
```
