from django.db import models
from catalogue.models import Tag, Author, Book


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(
        max_length=63,
        unique_for_month='pub_date',
        help_text='A unique label for URL config.')
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    authors = models.ManyToManyField(Author, related_name='blog_posts')
    books = models.ManyToManyField(Book, related_name='blog_posts')

    def __str__(self):
        return "{} on {}".format(
            self.title,
            self.pub_date.strftime('%Y-%m-%d')
        )

    class Meta:
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'
