# Generated by Django 2.2 on 2019-05-09 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0004_auto_20190509_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='priority',
            field=models.CharField(choices=[('긴급', ''), ('중요', ''), ('보통', '')], default=1, max_length=5),
            preserve_default=False,
        ),
    ]
