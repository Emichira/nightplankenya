# Generated by Django 2.2 on 2019-07-12 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_auto_20190713_0115'),
        ('events', '0007_auto_20190712_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.Club'),
        ),
    ]
