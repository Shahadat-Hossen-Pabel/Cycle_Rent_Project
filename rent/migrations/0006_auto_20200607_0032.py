# Generated by Django 3.0.7 on 2020-06-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0005_bike_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='slug',
            field=models.SlugField(),
        ),
    ]
