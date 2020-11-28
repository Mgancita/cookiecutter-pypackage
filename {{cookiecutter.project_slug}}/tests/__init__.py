"""tests namespace."""

from {{cookiecutter.project_slug}} import __author__, __email__, __version__


def test_project_info():
    """Test __author__ value."""
    assert __author__ == "{{cookiecutter.full_name}}"
    assert __email__ == "{{cookiecutter.email}}"
    assert __version__ == "0.0.0"
