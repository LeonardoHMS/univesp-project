# Generated by Django 5.0.3 on 2024-03-29 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='type_of_cut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='schedule.typeofcut'),
        ),
    ]