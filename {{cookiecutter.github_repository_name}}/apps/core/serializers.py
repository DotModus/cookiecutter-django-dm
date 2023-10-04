from rest_framework import serializers

from . import models
class UserSerializer(serializers.ModelSerializer):
    """Basic serializer for User model."""
    class Meta:
        """Serialize all fields and exclude password from being read."""

        model = models.User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
