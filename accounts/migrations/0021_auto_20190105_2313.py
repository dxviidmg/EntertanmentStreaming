# Generated by Django 2.0.1 on 2019-01-06 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20190105_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
    ]
