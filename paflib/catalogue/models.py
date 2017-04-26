from django.db import models
from django.core.urlresolvers import reverse

class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A unique label for URL config.')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse(
            'catalogue_tag_detail',
            kwargs={'slug': self.slug}
        )


class Author(models.Model):
    first_name = models.CharField('first name', max_length=63)
    last_name = models.CharField('last name', max_length=63)
    birth_date = models.DateField('date of birth')
    slug = models.SlugField(
        max_length=127,
        unique=True,
        help_text='A unique label for URL config.')

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return "{} {} ({})".format(
            self.first_name.title(),
            self.last_name.title(),
            self.birth_date
        )

    def get_absolute_url(self):
        return reverse(
            'catalogue_author_detail',
            kwargs={'slug': self.slug}
        )


class Book(models.Model):
    title = models.CharField(max_length=1023)
    authors = models.ManyToManyField(Author, related_name='books')
    slug = models.SlugField(
        max_length=1023,
        unique=True,
        help_text='A unique label for URL config.')
    pub_date = models.DateField('date published')
    publisher = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag, related_name='books')
    location = models.CharField(max_length=1023)
    status = models.CharField(max_length=63)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return "{} at location: {}".format(
            self.title,
            self.location
        )

    def get_absolute_url(self):
        return reverse(
            'catalogue_book_detail',
            kwargs={'slug': self.slug}
        )
