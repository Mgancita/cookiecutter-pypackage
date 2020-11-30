# Cookiecutter PyPackage

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a Python package. Powered by Poetry, GitHub actions, and MkDocs-Material.

## Introduction
Welcome to cookiecutter-pypackage! The creation of this project was inspired by the want for an easy-to-configure repository setup where everything could be done within GitHub. In the current state, the repositories created from the cookiecutter uses only GitHub for continuous integration and continuous deployment (CI/CD) via GitHub Actions. This allows for developers to create, test, and deploy their package(s) in an easy-to-use and easy-to-maintain way. 

## Features
This template has the following features:  

  - [`pytest`](https://github.com/pytest-dev/pytest): Unit and coverage testing  
  - [`flake8`](https://github.com/PyCQA/flake8) and [`pylint`](https://github.com/PyCQA/pylint): Python style checks  
  - [`black`](https://github.com/psf/black): Auto-formatted code  
  - [`mypy`](https://github.com/python/mypy): Type checking  
  - [`Poetry`](https://github.com/python-poetry/poetry): Depedency management and packaging  
  - [`GitHub Actions`](https://github.com/features/actions): Automated CI checks, auto-release to PyPi, and automated version bumping (no more Travis needed)  
  - [`MkDocs-Material`](https://github.com/squidfunk/mkdocs-material): Auto-publish documentation to it's own webpage  

This is a simple list, for a deep-dive into why and how each feature is used visit [feature explanation](advanced/feature_explanation). If already familiar or just not interested, continue to [Getting started](getting-started/create_local_project).
