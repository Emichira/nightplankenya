# Generated by Django 2.2.3 on 2020-06-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='video_tutorial',
            field=models.URLField(blank=True, null=True),
        ),
    ]
