from django import forms
from django.core.exceptions import ValidationError

from .models import Tag, Author, Book


class SlugCleanMixin:
    # Mixin Class for Slug Clean Method.
    def clean_slug(self):
        new_slug = (
            self.cleaned_data['slug'].lower()
        )
        if new_slug == 'create':
            raise ValidationError(
                'Slug may not be "create".'
            )
        return new_slug



class TagForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()


class AuthorForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
