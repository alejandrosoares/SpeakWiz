# Generated by Django 4.2.3 on 2023-09-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]
