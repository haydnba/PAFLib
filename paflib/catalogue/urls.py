from django.conf.urls import url

from .views import (
    # tag_list, tag_detail, tag_create,
    TagList, TagDetail, TagCreate,
    author_list, author_detail,
    # AuthorCreate,
    book_list, book_detail
    # BookCreate
)


urlpatterns = [
    url(r'^tag/$',
        TagList.as_view(),
        name='catalogue_tag_list'),
    url(r'^tag/create/$',
        TagCreate.as_view(),
        name='catalogue_tag_create'),
    url(r'^tag/(?P<slug>[\w\-]+)/$',
        TagDetail.as_view(),
        name='catalogue_tag_detail'),
    url(r'^author/$',
        author_list,
        name='catalogue_author_list'),
    # url(r'^author/create/$',
    #     AuthorCreate.as_view(),
    #     name='catalogue_author_create'),
    url(r'^author/(?P<slug>[\w\-]+)/$',
        author_detail,
        name='catalogue_author_detail'),
    url(r'^book/$',
        book_list,
        name='catalogue_book_list'),
    # url(r'^book/create/$',
    #     BookCreate.as_view(),
    #     name='catalogue_book_create'),
    url(r'^book/(?P<slug>[\w\-]+)/$',
        book_detail,
        name='catalogue_book_detail'),
]
