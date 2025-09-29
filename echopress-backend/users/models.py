from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=150, unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(min_length=8)
    date_joined=models.DateTimeField(auto_now_add=True)
    role=models.CharField(max_length=50, default='user')  # roles: user, admin, moderator
    is_active=models.BooleanField(default=True)

    bio = models.TextField(blank=True, null=True)  # Présentation
    website = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username