# Generated by Django 4.2.3 on 2023-09-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0006_rename_enable_topic_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='autogenerated',
            field=models.BooleanField(default=False),
        ),
    ]