# Generated by Django 3.0.6 on 2020-05-19 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagesneakers',
            name='name',
            field=models.CharField(default='sneakers', max_length=100),
        ),
    ]