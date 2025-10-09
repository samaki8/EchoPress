from rest_framework import serializers
from .models import Visitor

class visitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ['id', 'article', 'user', 'ip_address', 'visit_time', 'user_agent', 'referrer', 'path', 'is_bot']
        read_only_fields = ['ip_address', 'visit_time']
        