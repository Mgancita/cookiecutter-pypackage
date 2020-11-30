# Publish to PyPI

## Differences in the process
Now that we've published to test pypi. PyPI should be cake! Instead of re-writing the process with a few tweaks I'll mention the main differences here for getting to PyPI.

1. Visit [PyPI](https://www.pypi.org) (not test pypi) to create an account
2. Set the given username and password as `PYPI_USERNAME` and `PYPI_PASSWORD`.
3. For release: 
    - Select `master branch`, 
    - Set tag version to `0.1.0`, 
    - Set release title to `v0.1.0`, 
    - Do **NOT** select "This is pre-release".

The `pip` command should be:  

`$ pip install your_package_name`

or

`$ pip install your_package_name==0.1.0`

if you wish to pin the version number.

And that's it! Checkout the Advanced section if you'd like to learn more about the specific quality checks being used to test the code as well as why certain packages were used over others in this repository.
