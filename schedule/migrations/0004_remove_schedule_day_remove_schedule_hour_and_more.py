# Generated by Django 5.0.3 on 2024-04-07 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_alter_typeofcut_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='day',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='hour',
        ),
        migrations.AddField(
            model_name='schedule',
            name='date_hour',
            field=models.DateTimeField(null=True),
        ),
    ]
