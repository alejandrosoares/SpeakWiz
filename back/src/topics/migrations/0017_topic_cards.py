# Generated by Django 4.2.3 on 2025-03-06 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0016_rename_created_topiccard_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='cards',
            field=models.JSONField(default=list),
        ),
    ]
