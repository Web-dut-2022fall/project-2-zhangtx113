# Generated by Django 3.1.6 on 2021-03-22 00:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20210322_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='hbidder',
        ),
        migrations.AddField(
            model_name='item',
            name='watchers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]