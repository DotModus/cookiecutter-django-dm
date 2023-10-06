import os

from django.core.management.base import BaseCommand

from apps.core.models import User
class Command(BaseCommand):
    """Base Command class"""

    help = 'Create a superuser if it does not exist'
    password = os.getenv('DJANGO_ADMIN_PASSWORD')
    username = os.getenv('DJANGO_ADMIN_USERNAME', 'admin')

    def handle(self, *args, **kwargs):
        """Create superuser if it does not exist"""
        if not User.objects.filter(username=self.username).exists():
            User.objects.create_superuser(self.username, 'admin@example.com',
                                          self.password)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
