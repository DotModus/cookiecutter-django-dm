import os

from apps.core.models import User
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    """Base Command class"""

    help = 'Create a superuser if it does not exist'
    password = os.getenv('DJANGO_ADMIN_PASSWORD', None)
    username = os.getenv('DJANGO_ADMIN_USERNAME', 'admin')
    if not password:
        raise ValueError('DJANGO_ADMIN_PASSWORD environment variable is not set')
    def handle(self, *args, **kwargs):
        """Create superuser if it does not exist"""
        password = os.getenv('DJANGO_ADMIN_PASSWORD', None)
        username = os.getenv('DJANGO_ADMIN_USERNAME', 'admin')
        if not password:
            raise ValueError(
                'DJANGO_ADMIN_PASSWORD environment variable not set')
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username,
                                          f'{username}@example.com',
                                          password)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
