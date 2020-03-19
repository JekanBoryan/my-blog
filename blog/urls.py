from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/$', views.PostListView.as_view(), name='posts'),
    url(r'^posts/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]
