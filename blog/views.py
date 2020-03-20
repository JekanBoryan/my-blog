from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Author, Comment
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


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


class CommentCreate(LoginRequiredMixin, generic.CreateView):
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        form.instance.author = self.request.user.author
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk']})


