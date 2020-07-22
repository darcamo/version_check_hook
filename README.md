# version_check_hook

A pre-commit hook that checks the version in `pyproject.toml` is the same as in a `__init__.py` file

This is useful if you develop a python library with a directory structure similar to the one below

    pyproject.toml  <- Defines the version of the library
    library_name
       __init__.py  <- This file defines a "__version__" variable containing the library version
       other_files_and_folders
    .pre-commit-config.yaml
    other_files_and_folders

and you want to make sure that you never forget to update the `__version__`
variable when you change the library version in the `pyproject.toml` file.

**Note**: the name of folder containing the `__init__.py` file with the
`__version__` variable must be exactly the same name of the library defined in
the `pyproject.toml` file.

In order to use this, add this to you `.pre-commit-config.yaml` file

```yaml
repos:
- repo: https://github.com/darcamo/version_check_hook.git
  rev: v1.2
  hooks:
  - id: version_check
```
