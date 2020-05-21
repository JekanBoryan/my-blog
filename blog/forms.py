from .models import Comment, Author
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

