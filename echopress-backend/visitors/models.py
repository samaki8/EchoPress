#visitors/models.py
from django.db import models
from django.conf import settings

# Create your models here.
class Visitor(models.Model):
    article = models.ForeignKey('articles.Article', null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    ip_address = models.GenericIPAddressField()
    visit_time = models.DateTimeField(auto_now_add=True, db_index=True)
    user_agent = models.CharField(max_length=512, blank=True)
    referrer = models.URLField(blank=True)
    path = models.CharField(max_length=512, blank=True)
    session_key = models.CharField(max_length=40, blank=True, db_index=True)
    is_bot = models.BooleanField(default=False)
    extra = models.JSONField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['article', 'visit_time']),        # recherches par article triées par date
            models.Index(fields=['is_bot', 'visit_time']),         # filtrer bots puis trier
        ]


    def __str__(self):
        return f"Visitor {self.ip_address} at {self.visit_time}"