# Generated by Django 4.2.3 on 2024-03-15 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='name',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]
