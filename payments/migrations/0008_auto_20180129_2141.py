# Generated by Django 2.0.1 on 2018-01-30 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_auto_20180125_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='validity_month',
            field=models.CharField(choices=[('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], max_length=20),
        ),
    ]
