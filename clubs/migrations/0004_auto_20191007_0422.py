# Generated by Django 2.2.3 on 2019-10-07 01:22

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0003_auto_20190714_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='club_cover_image',
            field=models.ImageField(blank=True, upload_to='images/event/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='club',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]