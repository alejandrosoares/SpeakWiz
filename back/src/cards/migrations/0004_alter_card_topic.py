# Generated by Django 4.2.3 on 2023-10-02 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0008_remove_topic_number_questions'),
        ('cards', '0003_remove_card_enable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.topic'),
        ),
    ]
