# Generated by Django 5.1.4 on 2025-01-08 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_todo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
