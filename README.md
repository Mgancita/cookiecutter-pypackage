# Cookiecutter PyPackage

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a Python package. Powered by Poetry, GitHub actions, and MkDocs-Material.

## Features
This template has the following features:
  - [`pytest`](https://github.com/pytest-dev/pytest): Unit and coverage testing
  - [`flake8`](https://github.com/PyCQA/flake8) and [`pylint`](https://github.com/PyCQA/pylint): Python style checks
  - [`black`](https://github.com/psf/black): Auto-formatted code
  - [`mypy`](https://github.com/python/mypy): Type checking
  - [`Poetry`](https://github.com/python-poetry/poetry): Depedency managemnt and packaging
  - [`GitHub Actions`](https://github.com/features/actions): Automated CI checks, auto-release to PyPi, and automated version bumping (no more Travis needed)
  - [`MkDocs-Material`](https://github.com/squidfunk/mkdocs-material): Auto-publish documentation to it's own webpage

## Quickstart
Install the latest Cookiecutter if you haven't installed it yet (this requires
`Cookiecutter 1.4.0` or higher):

`$ pip install -U cookiecutter>=1.4.0`

Generate a Python package project:

`$ cookiecutter https://github.com/mgancita/cookiecutter-pypackage.git`

