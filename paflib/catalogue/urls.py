from django.conf.urls import url

from .views import (
    tag_list, tag_detail,
    author_list, author_detail,
    book_list, book_detail
)


urlpatterns = [
    url(r'^tag/$',
        tag_list,
        name='catalogue_tag_list'),
    url(r'^tag/(?P<slug>[\w\-]+)/$',
        tag_detail,
        name='catalogue_tag_detail'),
    url(r'^author/$',
        author_list,
        name='catalogue_author_list'),
    url(r'^author/(?P<slug>[\w\-]+)/$',
        author_detail,
        name='catalogue_author_detail'),
    url(r'^book/$',
        book_list,
        name='catalogue_book_list'),
    url(r'^book/(?P<slug>[\w\-]+)/$',
        book_detail,
        name='catalogue_book_detail'),
]
