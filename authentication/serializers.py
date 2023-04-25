from rest_framework import serializers

from authentication import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'email']
        read_only_fields = ['first_name', 'last_name', 'email']
