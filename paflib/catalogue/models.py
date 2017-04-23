from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A unique label for URL config.')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    first_name = models.CharField('first name', max_length=63)
    last_name = models.CharField('last name', max_length=63)
    birth_date = models.DateField('date of birth')
    slug = models.SlugField(
        max_length=127,
        unique=True,
        help_text='A unique label for URL config.')

    def __str__(self):
        return "{} {} ({})".format(
            self.first_name,
            self.last_name,
            self.birth_date
        )

    class Meta:
        ordering = ['last_name']


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

    def __str__(self):
        return "{} at location: {}".format(
            self.title,
            self.location
        )

    class Meta:
        ordering = ['title']
