# Generated by Django 4.0.4 on 2022-05-16 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
