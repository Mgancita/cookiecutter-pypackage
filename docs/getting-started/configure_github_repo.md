# Configure GitHub repository

## Setup branches
Now that we've pushed our repository to GitHub we'll see a `main` branch with all the code but you rarely want to push code directly to main. To mitigate this, lets create a `development` branch for which to actively develop code and then move it to main once we think it's safe for production. To do so, simply: 

1. Click on the "main" dropdown button your repo's homepage
2. Type in "development" in the search bar
3. Select "Create branch: development from main".

**Note if 'development' is not used. You must change the branch reference in certain files within the '.github/workflows' directory for CI checks to work.**

As seen with main, you'll see Actions being run for development. Additionally, whenever you open a pull request (PR) from development to main, the checks will automatically run to make sure the code is safe for merging.

That is the base needed for the CI system to work. If you wish to add further protection to your repository visit the `Settings -> Branches` section of your repo. This will allow you to add things like not allow code into a certain branch until it passes all CI checks and/or has been approved by at least 1 admin/contributer.

## Setup documentation page
As mentioned in the previous section, your repo magically (done by Github Actions) created a `gh-pages` branch. All the files in that branch are automatically generated from the files in the repository's `docs` folder. For more information on how to add pages to this documentation visit [MkDocs-Material docs](https://squidfunk.github.io/mkdocs-material/).

To publish the docs to your own github site do the following:

1. Go to "Settings" section.
2. Scroll down to "GitHub Pages" section.
3. Within the "Source" section select `gh-pages` branch and `/(root)`.
4. Click "Save" button.

Scroll back down to "GitHub Pages" and a link should be given for where your docs will be published (wait a few minutes for publication). In addition, this link can be added in the `About` section of your repository under "website" to display the link in a nice area.

Now your repository has been properly configured! With proper code quality checks and automatically publishing documentation, you're just one more step away to having the infrastructure to develop an open-source Python package.
