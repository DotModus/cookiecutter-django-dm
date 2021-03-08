from  django.core.management.utils import get_random_secret_key

with open('{{cookiecutter.github_repository_name}}/.env', 'w') as env_file:
    env_file.write(
        f"SECRET_KEY={get_random_secret_key()}\n"
        f"DATABASE_ENGINE=django.db.backends.postgresql\n"
        f"DATABASE_NAME=cookie_local\n"
        f"DATABASE_USER=cookie\n"
        f"DATABASE_PASSWORD=cookie\n"
        f"DATABASE_HOST=127.0.0.1\n"
        f"DATABASE_PORT=5432\n"
    )
