# Generated by Django 4.2.3 on 2025-03-14 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0023_rename_tag_topictag_title_remove_topictag_topics_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="topic",
            old_name="autogenerated",
            new_name="is_autogenerated",
        ),
        migrations.RenameField(
            model_name="topic",
            old_name="enabled",
            new_name="is_enabled",
        ),
        migrations.RenameField(
            model_name="topic",
            old_name="premium",
            new_name="is_premium",
        ),
    ]
