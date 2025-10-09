from django.db import models
from django.conf import settings

class CallNow(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='calls')
    visitor_ip = models.GenericIPAddressField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    scheduled_at = models.DateTimeField()  # Date et heure à laquelle l'appel doit être fait
    created_at = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"CallNow request for {self.phone_number} scheduled at {self.scheduled_at}"
