# Generated by Django 2.2.2 on 2019-07-26 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PublicationAdd', '0003_auto_20190726_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='DelayedPosting',
            field=models.DateField(default=datetime.date(2019, 7, 26)),
        ),
    ]
