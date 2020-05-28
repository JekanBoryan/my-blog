from rest_framework import serializers
from django.contrib.auth.models import User

from ..models import Author, Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class AuthorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'username', 'bio']


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='blogger.user.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author_name', 'title', 'text', 'pub_date']


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.user.username', read_only=True)
    post_title = serializers.CharField(source='post.title', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post_title', 'author_name', 'text', 'pub_date']
