# Generated by Django 2.1 on 2021-09-01 15:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20210221_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='date_expired',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 8, 16, 28, 42, 743058)),
        ),
    ]
