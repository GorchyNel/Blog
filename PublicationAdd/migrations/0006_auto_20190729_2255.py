# Generated by Django 2.2.3 on 2019-07-29 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PublicationAdd', '0005_auto_20190728_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='DateOfPublic',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 29, 22, 55, 5, 369413)),
        ),
    ]