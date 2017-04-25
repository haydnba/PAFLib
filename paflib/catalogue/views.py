from django.shortcuts import get_object_or_404, render

from .models import Tag, Author, Book


def tag_list(request):
    return render(
        request,
        'catalogue/tag_list.html',
        {'tag_list': Tag.objects.all()}
    )

def tag_detail(request, slug):
    tag = get_object_or_404(
        Tag, slug__iexact=slug
    )
    return render(
        request,
        'catalogue/tag_detail.html',
        {'tag': tag}
    )

def author_list(request):
    return render(
        request,
        'catalogue/author_list.html',
        {'author_list': Author.objects.all()}
    )

def author_detail(request, slug):
    author = get_object_or_404(
        Author, slug__iexact=slug
    )
    return render(
        request,
        'catalogue/author_detail.html',
        {'author': author}
    )

def book_list(request):
    return render(
        request,
        'catalogue/book_list.html',
        {'book_list': Book.objects.all()}
    )

def book_detail(request, slug):
    book = get_object_or_404(
        Book, slug__iexact=slug
    )
    return render(
        request,
        'catalogue/book_detail.html',
        {'book': book}
    )
