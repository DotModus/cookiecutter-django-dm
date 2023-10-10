FROM python:3.10
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Adds our application code to the image
COPY . /opt/{{cookiecutter.github_repository_name}}
WORKDIR /opt/{{cookiecutter.github_repository_name}}

RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Run the production server
CMD gunicorn --bind 0.0.0.0:8000 --access-logfile - {{cookiecutter.github_repository_name}}.wsgi:application
