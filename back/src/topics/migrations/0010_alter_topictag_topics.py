# Generated by Django 4.2.3 on 2023-11-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0009_topictag_number_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topictag',
            name='topics',
            field=models.ManyToManyField(blank=True, to='topics.topic'),
        ),
    ]
