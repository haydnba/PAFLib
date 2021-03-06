# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-04-23 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(help_text='A unique label for URL config.', max_length=63, unique_for_month='pub_date')),
                ('text', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='date published')),
                ('authors', models.ManyToManyField(related_name='blog_posts', to='catalogue.Author')),
                ('books', models.ManyToManyField(related_name='blog_posts', to='catalogue.Book')),
                ('tags', models.ManyToManyField(related_name='blog_posts', to='catalogue.Tag')),
            ],
            options={
                'ordering': ['-pub_date', 'title'],
                'get_latest_by': 'pub_date',
            },
        ),
    ]
