# Generated by Django 2.0.1 on 2018-01-21 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='logo',
            field=models.ImageField(upload_to='movies/%Y/%m/%d/'),
        ),
    ]