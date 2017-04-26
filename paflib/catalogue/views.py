from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect, render

from .models import Tag, Author, Book
from .forms import TagForm, AuthorForm, BookForm


# def tag_list(request):
#     return render(
#         request,
#         'catalogue/tag_list.html',
#         {'tag_list': Tag.objects.all()}
#     )
#
# def tag_detail(request, slug):
#     tag = get_object_or_404(
#         Tag, slug__iexact=slug
#     )
#     return render(
#         request,
#         'catalogue/tag_detail.html',
#         {'tag': tag}
#     )
#
# def tag_create(request):
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             new_tag = form.save()
#             return redirect(new_tag)
#     else:
#         form = TagForm()
#     return render(
#         request,
#         'catalogue/tag_form.html',
#         {'form': form}
#     )


class TagList(View):
    template_name = 'catalogue/tag_list.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'tag_list': Tag.objects.all()}
        )


class TagDetail(View):
    template_name = 'catalogue/tag_detail.html'

    def get(self, request, slug):
        tag = get_object_or_404(
            Tag,
            slug__iexact=slug
        )
        return render(
            request,
            self.template_name,
            {'tag': tag}
        )


class TagCreate(View):
    form_class = TagForm
    template_name = 'catalogue/tag_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class()}
        )

    def post(self,request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        else:
            return render(
                request,
                self.template_name,
                {'form': bound_form}
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

# class AuthorCreate(View):
#     form_class = authorForm
#     template_name = 'catalogue/author_form.html'
#
#     def get(self, request):
#         return render(
#             request,
#             self.template_name,
#             {'form': self.form_class()}
#         )
#
#     def post(self,request):
#         bound_form = self.form_class(request.POST)
#         if bound_form.is_valid():
#             new_tag = bound_form.save()
#             return redirect(new_tag)
#         else:
#             return render(
#                 request,
#                 self.template_name,
#                 {'form': bound_form}
#             )

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

# class BookCreate(View):
#     form_class = BookForm
#     template_name = 'catalogue/book_form.html'
#
#     def get(self, request):
#         return render(
#             request,
#             self.template_name,
#             {'form': self.form_class()}
#         )
#
#     def post(self,request):
#         bound_form = self.form_class(request.POST)
#         if bound_form.is_valid():
#             new_tag = bound_form.save()
#             return redirect(new_tag)
#         else:
#             return render(
#                 request,
#                 self.template_name,
#                 {'form': bound_form}
#             )
