# Generated by Django 5.0.3 on 2024-05-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_schedule_obs'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='conclude',
            field=models.BooleanField(null=True),
        ),
    ]