""" from django.db import models
from django.conf import settings

class Notification(models.Model):
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=50) 

    def __str__(self):
        return f"Notification for {self.recipient.username}: {self.title}"""

# notifications/models.pyfrom django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ("ARTICLE", "Nouvel article"),
        ("COMMENT_REPLY", "Réponse à un commentaire"),
        ("LIKE", "Like sur un article/commentaire"),
        ("CALL", "Appel entrant"),
        ("LIVE_INVITE", "Invitation à un live/chat"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    title = models.CharField(max_length=255)
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    url = models.URLField(blank=True, null=True)  # Pour accéder à l’élément concerné (article, chat, appel, etc.)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.title}"