# Generated by Django 2.2 on 2019-04-23 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0002_auto_20190422_1848'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]