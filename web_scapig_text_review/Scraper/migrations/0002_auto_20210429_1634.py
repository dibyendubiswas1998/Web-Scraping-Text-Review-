# Generated by Django 3.2 on 2021-04-29 11:04

import Scraper.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scraper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review_details',
            name='customer_comment',
        ),
        migrations.RemoveField(
            model_name='review_details',
            name='customer_name',
        ),
        migrations.RemoveField(
            model_name='review_details',
            name='customer_rating',
        ),
        migrations.RemoveField(
            model_name='review_details',
            name='customer_review',
        ),
        migrations.AddField(
            model_name='review_details',
            name='json_data',
            field=models.JSONField(default=Scraper.models.my_default),
        ),
    ]