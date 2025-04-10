# Generated by Django 4.2.3 on 2025-03-07 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('llm_settings', '0003_setupevaluation_remove_llmsetupevaluation_llm_setup_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicGeneratorSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('template_variables', models.JSONField(default=list)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='llm_settings.llmmodel')),
                ('prompt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='llm_settings.prompt')),
            ],
            options={
                'abstract': False,
                'unique_together': {('model', 'prompt')},
            },
        ),
    ]
