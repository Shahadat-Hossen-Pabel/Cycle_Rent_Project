# Generated by Django 3.0.7 on 2020-06-08 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0018_finalrent_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='notuse',
            name='title',
            field=models.CharField(default='gh', max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notuse',
            name='dont_use',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rent.SelectPoint'),
        ),
    ]
