# Publish to PyPI

## Differences in the process
Now that we've published to test pypi. PyPI should be cake! Instead of re-writing the process with a few tweaks I'll mention the main differences here for getting to PyPI.

1. Visit [PyPI](https://www.pypi.org) (not test pypi) to create an account.
2. Go to the `API tokens` section with [Account Settings](https://pypi.org/manage/account/).
3. Generate a new API token and set it as `PYPI_TOKEN`.
    - Note that it should have a prefix of `pypi-` before a long token of characters.
3. For release: 
    - Select `main branch`, 
    - Set tag version to `0.1.0`, 
    - Set release title to `v0.1.0`, 
    - Do **NOT** select "This is pre-release".

The `pip` command should be:  

`$ pip install your_package_name`

or

`$ pip install your_package_name==0.1.0`

if you wish to pin the version number.

## Use your code

Lastly, lets see how you would import your code. Lets say you have a package called test_project, with a module called test_file, and within that module a class called TestClass. After pip installing your code, in a Python file you could import the class like so,  

`from test_project.test_file import TestClass`

And that's it! Checkout the Advanced section if you'd like to learn more about the specific quality checks being used to test the code as well as why certain packages were used over others in this repository.
