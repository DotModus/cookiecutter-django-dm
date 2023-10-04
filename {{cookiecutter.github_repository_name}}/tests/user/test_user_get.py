"""This module contains tests for the User model."""
import pytest
from django.test import Client

from apps.core.models import User


def test_user_get_not_logged_in() -> None:
    """Test that a user can be retrieved."""
    client = Client()
    response = client.get('/users/')

    assert response.status_code == 401

@pytest.mark.django_db
def test_user_get_logged_in(logged_in_user: User) -> None:
    """Test that a user can be retrieved."""
    client = Client()
    client.force_login(logged_in_user)
    response = client.get('/users/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_user_get_logged_in_admin(logged_in_admin: User) -> None:
    """Test that a user can be retrieved."""
    client = Client()
    client.force_login(logged_in_admin)
    response = client.get('/users/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_is_admin(logged_in_user: User,
                  logged_in_admin: User) -> None:
    """Test that a user is marked correctly as admin."""
    assert logged_in_user.is_admin is False
    assert logged_in_admin.is_admin
