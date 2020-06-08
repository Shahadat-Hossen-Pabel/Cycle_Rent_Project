# Generated by Django 3.0.7 on 2020-06-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0011_pickuppoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_point', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='pickuppoint',
            name='select_point',
        ),
    ]
