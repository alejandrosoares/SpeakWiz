# Generated by Django 4.2.3 on 2023-11-15 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0008_remove_topic_number_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='topictag',
            name='number_topics',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
