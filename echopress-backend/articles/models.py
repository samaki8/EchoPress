#articles/models.py
from email.mime import image
from unicodedata import category
from django.db import models
from django.conf import settings

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    video = models.FileField(upload_to='article_videos/', null=True, blank=True)
    nbr_views = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
    


    def __str__(self):
        return self.title
