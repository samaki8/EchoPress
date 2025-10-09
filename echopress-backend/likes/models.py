from django.db import models
from django.conf import settings
from articles.models import Tag

class Like(models.Model):
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE, related_name='article_likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_likes')
    comment = models.ForeignKey('comments.Comment', null=True, blank=True, on_delete=models.CASCADE, related_name='comment_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'article'), ('user', 'comment'))

    def __str__(self):
        target = self.article if self.article else self.comment
        return f"Like by {self.user.username} on {target}"
