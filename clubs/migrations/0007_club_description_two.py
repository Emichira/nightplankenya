# Generated by Django 2.2.3 on 2019-10-15 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0006_club_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='description_two',
            field=models.TextField(null=True),
        ),
    ]
