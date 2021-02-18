from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager.

    Email is the unique identifiers for authentication instead of username.
    """

    def create_user(self, email: str, password: str, username: str,
                    **extra_fields):
        """
        Create and save a User with the given username, email and password.

        :param email: User email address.
        :param password: User password.
        :param username: User username.
        :param extra_fields: Optional extra User model fields.
        :return: Persisted User model
        """
        if not email:
            raise ValueError('The Email must be set')

        if not username:
            raise ValueError('The username must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, password: str, username: str,
                         **extra_fields):
        """
        Create and save a superuser with username, email and password.

        :param email: User email address.
        :param password: User password.
        :param username: User username.
        :param extra_fields: Optional extra User model fields.
        :return: Persisted User model
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')
        return self.create_user(email, password, username, **extra_fields)


class User(AbstractUser):
    """Custom User model. Email address is used for authentication."""

    email = models.EmailField('email address', unique=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']
    # objects = CustomUserManager()

    class Meta:
        """Override default meta attributes of User model."""

        ordering = ['-id']

    @property
    def is_admin(self):
        """Whether user has elevated privileges."""
        return self.is_staff or self.is_superuser
