from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Author, Comment
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.urls import reverse
from .forms import CommentForm
from django.http import HttpResponseForbidden


def index(request):
    num_posts = Post.objects.count()
    num_authors = User.objects.count()

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


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk']})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        form = self.get_form()
        if form.is_valid():
            new_comment_text = form.cleaned_data['text']
            new_comment_post = Post.objects.get(pk=self.kwargs['pk'])
            new_comment_author = request.user.author
            new_comment = Comment.objects.create(author=new_comment_author, post=new_comment_post, text=new_comment_text)
            new_comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5
    template_name = 'blog/author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author
