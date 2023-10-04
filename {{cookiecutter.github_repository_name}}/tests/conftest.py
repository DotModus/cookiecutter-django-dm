import pytest
from django.test import Client

from apps.core.models import User

@pytest.fixture
def django_db_setup(transactional_db) -> None:
    """Load fixtures into the database."""
    user = User.objects.create_user(username='user',
                                    email='user@user.com',
                                    password='user')
    user.save()
    admin = User.objects.create_superuser(username='admin',
                                          email='admin@admin.com',
                                          password='admin')
    admin.save()


@pytest.fixture
def logged_in_user(client: Client) -> User:
    """Login user on the client object."""
    client = client or Client()
    user = User.objects.get(username='user')
    client.force_login(user)
    return user


@pytest.fixture
def logged_in_admin(client: Client) -> User:
    """Login an admin user on the client object."""
    client = client or Client()
    user = User.objects.get(username='admin')
    client.force_login(user)
    return user
