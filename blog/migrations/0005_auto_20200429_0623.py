# Generated by Django 2.2.5 on 2020-04-29 06:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200127_0228'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='course_category',
            field=models.CharField(choices=[('math', 'Math'), ('stat', 'Stat'), ('csc', 'CSC'), ('seng', 'SENG'), ('other', 'Other')], default='Other', max_length=6),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 29, 6, 23, 51, 532072, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 29, 6, 23, 51, 531591, tzinfo=utc)),
        ),
    ]
