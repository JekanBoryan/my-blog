from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^posts/$', views.PostListCreateView.as_view()),
    url(r'^posts/(?P<pk>\d+)$', views.PostSingleView.as_view()),
    url(r'^authors/$', views.AuthorListView.as_view()),
    url(r'^authors/(?P<pk>\d+)$', views.AuthorSingleView.as_view()),
    url(r'^comments/$', views.CommentListCreateView.as_view()),
    url(r'^comments/(?P<pk>\d+)$', views.CommentSingleView.as_view()),
]