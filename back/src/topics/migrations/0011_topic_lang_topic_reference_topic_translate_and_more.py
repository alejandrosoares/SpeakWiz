# Generated by Django 4.2.3 on 2024-03-15 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0010_alter_topictag_topics'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='lang',
            field=models.CharField(choices=[('en', 'English'), ('es', 'Spanish'), ('de', 'German')], default='en', max_length=2),
        ),
        migrations.AddField(
            model_name='topic',
            name='reference',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='topics.topic'),
        ),
        migrations.AddField(
            model_name='topic',
            name='translate',
            field=models.BooleanField(default=False, help_text='If the topic has been translated to any language'),
        ),
        migrations.CreateModel(
            name='TopicTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translated_es', models.BooleanField(default=False)),
                ('translated_de', models.BooleanField(default=False)),
                ('topic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='topics.topic')),
            ],
        ),
    ]
