# Generated by Django 2.0.1 on 2018-02-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0012_auto_20180207_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='months',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=1),
        ),
    ]
