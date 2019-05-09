# Generated by Django 2.2 on 2019-05-09 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0005_feed_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='priority',
            field=models.CharField(choices=[('긴급', '긴급'), ('중요', '중요'), ('보통', '보통')], max_length=5),
        ),
    ]
