import random


def get_random_secret_key():
    is_prng = random.SystemRandom()
    allowed_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    length = 50
    return ''.join(random.choice(allowed_chars) for _ in range(length))


with open('.env', 'w') as env_file:
    env_file.write(
        f'SECRET_KEY="{get_random_secret_key()}"\n'
        'DATABASE_ENGINE=django.db.backends.postgresql\n'
        'DATABASE_NAME=cookie_local\n'
        'DATABASE_USER=cookie\n'
        'DATABASE_PASSWORD=cookie\n'
        'DATABASE_HOST=127.0.0.1\n'
        'DATABASE_PORT=5432\n'
        'DEBUG=True\n'
    )
