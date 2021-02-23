# define the name of the virtual environment directory
VENV := {{cookiecutter.virtual_env_name}}

.PHONY: all venv run clean virtualenv startup

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: virtualenv requirements.txt
	python3 -m virtualenv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

virtualenv:
	which virtualenv

# venv is a shortcut target
venv: $(VENV)/bin/activate

run: venv startup
	./$(VENV)/bin/python3 manage.py migrate
	./$(VENV)/bin/python3 manage.py runserver

startup: venv
	docker-compose up -d
	./$(VENV)/bin/python3 manage.py migrate
	./$(VENV)/bin/python3 manage.py createsuperuser

drop:
	docker-compose down -v

reset-virtualenv:
	python3 -m virtualenv --clear $(VENV)

clean-cached-python:
	find . -type f -name '*.pyc' -delete

