# Generated by Django 4.0.5 on 2022-07-15 04:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0013_alter_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 15, 4, 50, 20, 305973, tzinfo=utc)),
        ),
    ]
