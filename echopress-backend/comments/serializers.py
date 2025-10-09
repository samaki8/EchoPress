from rest_framework import serializers
from .models import Comment, CommentLike, CommentFile

#gère la sérialisation des fichiers liés aux commentaires.
class CommentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentFile
        fields = ['id', 'file', 'uploaded_at']

#affiche les likes avec l’auteur (champ user) et la date de création.
class CommentLikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = CommentLike
        fields = ['id', 'user', 'created_at']


# intègre les fichiers (files), l’auteur (user), et les likes (likes) liés au commentaire.
class CommentSerializer(serializers.ModelSerializer):
    files = CommentFileSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()
    likes = CommentLikeSerializer(many=True, read_only=True, source='direct_likes')

    class Meta:
        model = Comment
        fields = ['id', 'article', 'user', 'content', 'created_at', 'updated_at', 'parent', 'files', 'likes']
        read_only_fields = ['user']

        