from rest_framework import serializers
from .models import LiveChatMessage

class LiveChatMessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    recipient = serializers.StringRelatedField()

    class Meta:
        model = LiveChatMessage
        fields = ['id', 'sender', 'recipient', 'message', 'sent_at', 'read']
        read_only_fields = ['sender', 'recipient']