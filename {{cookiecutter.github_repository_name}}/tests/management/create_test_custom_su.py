import os
from io import StringIO

import pytest
from apps.core.models import User
from django.core.management import call_command


@pytest.mark.django_db
def test_create_superuser() -> None:
    """Test that a superuser can be created."""
    os.environ['DJANGO_ADMIN_PASSWORD'] = 'password'
    call_command('create_custom_superuser')
    assert User.objects.filter(username='admin').exists()


@pytest.mark.django_db
def test_create_superuser_no_password() -> None:
    """Test that an exception is raised if no password is set."""
    if 'DJANGO_ADMIN_PASSWORD' in os.environ:
        os.environ.pop('DJANGO_ADMIN_PASSWORD')
    with pytest.raises(ValueError):
        call_command('create_custom_superuser')



@pytest.mark.django_db
def test_create_superuser_already_exists() -> None:
    os.environ['DJANGO_ADMIN_PASSWORD'] = 'password'
    call_command('create_custom_superuser')
    out = StringIO()
    call_command('create_custom_superuser', stdout=out)
    assert 'Superuser already exists' in out.getvalue()
