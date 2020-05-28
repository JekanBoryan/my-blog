from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, get_object_or_404

from ..models import Author, Post, Comment
from django.contrib.auth.models import User
from .serializers import PostSerializer, AuthorSerializer, CommentSerializer


class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorSingleView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CommentListCreateView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        post = get_object_or_404(Post, id=self.request.data.get('post_id'))
        return serializer.save(author=author, post=post)


class CommentSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        blogger = get_object_or_404(Author, id=self.request.data.get('blogger_id'))
        return serializer.save(blogger=blogger)


class PostSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
