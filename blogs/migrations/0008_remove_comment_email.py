# Generated by Django 2.2.3 on 2020-06-05 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_comment_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
