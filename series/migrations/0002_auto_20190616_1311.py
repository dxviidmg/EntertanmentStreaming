# Generated by Django 2.0.1 on 2019-06-16 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='season',
            name='number',
            field=models.IntegerField(),
        ),
    ]
