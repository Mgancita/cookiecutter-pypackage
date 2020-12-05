{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![PyPI version](https://badge.fury.io/py/{{ cookiecutter.project_slug }}.svg)](https://badge.fury.io/py/{{ cookiecutter.project_slug }})
![versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)
[![GitHub license](https://img.shields.io/github/license/mgancita/{{ cookiecutter.project_slug }}.svg)](https://github.com/mgancita/{{ cookiecutter.project_slug }}/blob/master/LICENSE)
{% endif %}

{% if cookiecutter.use_black %}
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
{% endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
- Free software: {{ cookiecutter.open_source_license }}
- Documentation: https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug | replace("_", "-") }}.
{% endif %}

## Features

* TODO

## Credits


This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`mgancita/cookiecutter-pypackage`](https://mgancita.github.io/cookiecutter-pypackage/) project template.
