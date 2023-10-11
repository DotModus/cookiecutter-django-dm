# Create your viewsets here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
<<<<<<< HEAD
=======

>>>>>>> 2f8b90d (update files)
from . import models
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """User CRUD operations."""

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)
