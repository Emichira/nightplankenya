# Generated by Django 2.2 on 2019-07-14 14:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('counties', '0004_auto_20190712_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('genre_image', models.ImageField(upload_to='static/img/genre/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('is_published', models.BooleanField(default=True)),
                ('county', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='counties.County')),
            ],
        ),
    ]
