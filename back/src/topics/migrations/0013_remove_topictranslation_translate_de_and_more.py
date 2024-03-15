# Generated by Django 4.2.3 on 2024-03-15 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0003_alter_language_code_alter_language_name'),
        ('topics', '0012_remove_topictranslation_translated_de_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topictranslation',
            name='translate_de',
        ),
        migrations.RemoveField(
            model_name='topictranslation',
            name='translate_es',
        ),
        migrations.AddField(
            model_name='topictranslation',
            name='languages',
            field=models.ManyToManyField(blank=True, to='languages.language'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.language'),
        ),
    ]