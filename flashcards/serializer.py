from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

