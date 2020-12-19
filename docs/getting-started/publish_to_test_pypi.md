# Publish to test PyPI

## What is PyPI?
Great question! Python Package Index ([PyPI](https://www.pypi.org)) is where your computer goes (by default) when you `pip install` a package. By having your package on PyPI (don't worry it's 100% free), anyone can download your code with a single line command. I think that's pretty amazing!

## Cookiecutter's release process
The cookiecutter creates a project which has a release action for release candidates and a seperate one for production releases. The logic for why is as follows, before merging into main (and releasing to production) the developer should develop the code on the `development` branch. With the `development` code thought to be ready for production, the developer would create a *release candidate* (otherwise known as *pre-release*) which ships the package to [test pypi](https://test.pypi.org). This is done so the package can be downloaded and user-tested without messing up the *release history* of your pypi package. In addition, it's typically recommended to only have production-ready code on your main branch.

With this being said, we'll have to create a pypi and test pypi account and configuration to have a robust packaging and testing process.

**Note the current release process uses username and password while token api key is recommended. I've been having issues getting tokens to work with poetry but it's a main priority to shift to a better system.**

## Create test PyPI account
Before we're able to start publishing packages, we'll have to setup accounts. Visit [test pypi](https://test.pypi.org) and sign-up for an account. Remember your username and password as it'll be needed later on.

## Setup repository secrets for test PyPI
Github Secrets is an amazing tools in which you can inject secret variables into your Github Actions without them being visible to the public, which is especially important for open-source projects. The cookiecutter's out-of-the-box continous deployment process to publish to test pypi looks for a few secret variables so we'll set those here.

Navigate to the `Settings -> Secrets` section of your repository and add the secrets `TEST_PYPI_USERNAME` and `TEST_PYPI_PASSWORD`. **If you use other variable names, you'll have to change the secret references in `.github/workflows/test_pypi_publish.yml`.**

## Create release candidate
The time has come. These are the steps needed to publish to test pypi:

1. Navigate to the `Releases` section of your repository.
2. Click "Create a new release".
3. Set `Tag version` to `0.1.0-rc0`.
4. Select `development` branch.
5. Set `Release title` to `Release Candidate: v0.1.0` (or a fun name).
6. Select "This is a pre-release"
7. Click "Publish release"

Wait a few minutes (or watch the Github Action) for it to be published then visit your [test pypi projects page](https://test.pypi.org/manage/projects/) to see the release.

## Install package
Now that you code is on test pypi it's as easy as `pip install` with one extra argument which is `--extra-index-url`. This allows pip to know to also check test pypi for your code. It should look like this:

`$ pip install your_package_name==0.1.0rc0 --extra-index-url=https://test.pypi.org/simple/`

As there is no release candidates (and therefore no `0.1.0rc0`) on pypi. This command would not be able to find the given release without the `extra-index-url`.

And there it is! Your own package installable with a single command. Let's move on to see how to get it on PyPI!
