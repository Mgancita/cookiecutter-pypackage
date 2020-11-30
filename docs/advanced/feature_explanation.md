# Feature Explanation

## Pytest
Pytest is the package used for unit and coverage testing within the cookiecutter. I've chosen it over `unittest` as I find it easier to use and understand the results of. In addition, I like the native fixture functionality of pytest and the `pytest-cov` extension (used for coverage testing).

## Flake8 and Pylint
Flake8 and Pylint are both linters developed by the Python Code Quality Authority ([PyCQA](https://github.com/PyCQA)). As pylint is typically more exhaustive I select it for the default. If you want to be excessive (as I am with my repos), add flake8 to be sure the proper style guides are followed. 

## Black
Black is my go-to code formatter. Although annoying in the beginning, I've grown to love black as it makes git diffs 100x easier. With strict and opionated formatting, it does all the tedious formatting you're too lazy to do and leaves your pull requests with only the important changes being highlighted.

## Mypy
Mypy is the official checker for type-hinting which was added in Python 3.6. I think type-hinting allows for way better readability of Python code. Additionally, it makes sure that variables being passed throughout your program are being correctly accounted for in terms of their type (passing a string of "1" when it should be 1 can cause issues down the line).

## Poetry
Poetry is the dependency manager and packager for the cookiecutter. As I've grown frusturated with older tools for Python packaging (setuptools, tox, etc.) I decided to give Poetry a try and it was 100% worth it. It comprises all the necessary settings into a single `pyproject.toml` file (instead of `setup.py/cfg`, `requirements.txt`, `MANIFEST.in`, etc.) which has growing use by the above packages (with pylint, pytest, and black already supporting). Poetry is one of the main reasons the CI files are short and sweet and the repository is not overrun with packaging files.

## Github Actions
GitHub Actions is still pretty new to the CI space and is probably the biggest split (with Poetry) I use from most Python repositories. The main reason for using GitHub Actions is it's free (up to 2,000/minutes a month) and it's where my code exists. A lot of open-source projects use TravisCI or other services which I think adds complexity to developing and maintaining a project.

## MkDocs-Material
MkDocs-Material is the theme, builder, and publisher (extending MkDocs) for the documentation. The ease-of-use (I think you're seeing a pattern) of developing and deploying the documentation is a big win. Being able to edit the .md files and see the changes in real-time is a huge win. Furthermore, I think the resulting pages are the most visually appealing of any documentation framework I've worked with.

*Note an ideal state would be to have versioning for the documentation but you have to be an MkDocs-Material insider for that at the moment so it isn't supported by default.*

## Development process
Although this isn't a *feature* per-se, I think it's important to address as it's how I built the cookiecutter structure. The main drive behind having the CI checks on the `master` and `development` branches is so these are typically "protected" from having bad code. In addition, having the test pypi before pypi allows for user-testing of a new release without pushing out code that isn't ready for production. Lastly, I have the documentation auto-publish when `master` is updated as I only put code to master when it's ready to be released.
