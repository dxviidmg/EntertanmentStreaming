# Generated by Django 2.0.1 on 2019-01-06 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20190105_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
