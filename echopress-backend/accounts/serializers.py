from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'avatar',
            'twitter', 'linkedin', 'instagram', 'website', 'password'
        ]
        read_only_fields = ['id']
        extra_kwargs = {
            'email': {'write_only': True},
            'password': {'write_only': True, 'min_length': 8}
        }
    