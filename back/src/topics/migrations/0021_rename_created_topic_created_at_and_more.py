# Generated by Django 4.2.3 on 2025-03-08 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0020_rename_cards_topic_questions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='updated',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='topic',
            name='enabled',
            field=models.BooleanField(default=False, help_text='Enable it once you have reviewed the content'),
        ),
    ]
