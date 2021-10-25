from rest_framework import serializers

from apps.users.models import User

class UserApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username','email'
