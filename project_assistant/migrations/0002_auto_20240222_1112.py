# Generated by Django 3.2.24 on 2024-02-22 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_assistant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttable',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studenttable',
            name='year',
            field=models.CharField(max_length=100),
        ),
    ]
