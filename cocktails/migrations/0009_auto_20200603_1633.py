# Generated by Django 2.2.3 on 2020-06-03 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0008_auto_20200603_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='block_quote',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]