# Generated by Django 3.2.25 on 2025-01-21 05:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0030_auto_20241212_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 21, 11, 4, 48, 454079)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 21, 11, 4, 48, 454079)),
        ),
    ]
