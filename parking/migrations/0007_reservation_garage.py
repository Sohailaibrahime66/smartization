# Generated by Django 5.2 on 2025-04-15 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0006_dashboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='garage',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='parking.garage'),
        ),
    ]
