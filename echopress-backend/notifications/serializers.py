from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    recipient = serializers.StringRelatedField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'title', 'message', 'created_at', 'read', 'notification_type', 'url']
        read_only_fields = ['recipient', 'created_at']
