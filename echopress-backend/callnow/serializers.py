from rest_framework import serializers
from .models import CallNow

class CallNowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = CallNow
        fields = ['id', 'user', 'visitor_ip', 'phone_number', 'scheduled_at', 'created_at', 'status', 'notes']
        read_only_fields = ['user', 'visitor_ip']
