# Generated by Django 2.0.1 on 2019-06-17 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0005_auto_20190616_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
