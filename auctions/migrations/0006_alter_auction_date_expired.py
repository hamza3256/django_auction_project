# Generated by Django 3.2.7 on 2021-09-01 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_auction_date_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='date_expired',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 8, 17, 24, 29, 220553)),
        ),
    ]