# {{cookiecutter.github_repository_name}}

# Local Development

Start the dev server for local development:
```bash

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```

To run tests:
```bash

pytest

coverage run -m pytest && coverage xml -o coverage.xml
```

To format your code according to standards:
```bash

# run this once off in root of project
pre-commit install

# run this everytime you want to format code
pre-commit run -a
```
