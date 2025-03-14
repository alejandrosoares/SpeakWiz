# Generated by Django 4.2.3 on 2025-03-09 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("topics", "0022_alter_topic_reference"),
    ]

    operations = [
        migrations.RenameField(
            model_name="topictag",
            old_name="tag",
            new_name="title",
        ),
        migrations.RemoveField(
            model_name="topictag",
            name="topics",
        ),
        migrations.AddField(
            model_name="topic",
            name="tag",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="topics.topictag",
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="TopicTranslation",
        ),
    ]
