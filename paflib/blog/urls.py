from django.conf.urls import url

from .views import PostList, PostDetail, PostCreate


urlpatterns = [
    url(r'^$',
        PostList.as_view(),
        name='blog_post_list'),
    url(r'^post/create/$',
        PostCreate.as_view(),
        name='blog_post_create'),
    url(r'^(?P<year>\d{4})/'
        r'^(?P<month>\d[1,2])/'
        r'^(?P<slug>[\w\-]+)/$',
        PostDetail.as_view(),
        name='blog_post_detail'),
]
