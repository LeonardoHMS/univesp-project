# Generated by Django 5.0.3 on 2024-05-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_rename_type_typeofcut_type_cut'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='obs',
            field=models.TextField(max_length=255, null=True),
        ),
    ]