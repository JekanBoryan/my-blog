from django.shortcuts import render
from django.views import generic
from .models import Post, Author
from django.contrib.auth.models import User


def index(request):
    num_posts = Post.objects.count()
    num_authors = User.objects.count() - 1

    return render(
        request,
        'index.html',
        context={
            'num_posts': num_posts,
            'num_authors': num_authors,
        }
    )


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5
    template_name = 'blog/author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author
