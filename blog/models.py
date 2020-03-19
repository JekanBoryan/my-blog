from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(help_text='Enter your bio here')

    def __str__(self):
        return self.user.username


class Post(models.Model):
    blogger = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, help_text='Enter title of post')
    text = models.TextField(help_text='Text of post')
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=256, help_text='Enter your comment here')
    pub_date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
