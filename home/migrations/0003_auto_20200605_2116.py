# Generated by Django 3.0.7 on 2020-06-05 15:16

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200604_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='back_image',
            field=models.ImageField(upload_to=home.models.image_upload_to_slider),
        ),
    ]