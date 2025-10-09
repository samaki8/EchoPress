from django.db import models
from django.conf import settings

class Comment(models.Model):
    article = models.ForeignKey('articles.Article', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.user.username} on {self.article.title}"
# Likes on comments
class CommentLike(models.Model):
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='direct_likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_direct_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'comment')
# Files attached to comments
class CommentFile(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='comment_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
# History of edits for comments
class CommentHistory(models.Model):
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='history')
    old_content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)

# Audit log for comment actions
class CommentAuditLog(models.Model):
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=50)  # ex : "created", "edited", "deleted"
    created_at = models.DateTimeField(auto_now_add=True)
# Log for banned comments or users
class BanLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', null=True, blank=True, on_delete=models.SET_NULL)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

