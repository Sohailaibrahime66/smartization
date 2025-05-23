# Generated by Django 5.2 on 2025-04-15 11:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.CharField(default=False, max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('DOB', models.DateField(default=django.utils.timezone.now)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('national_id', models.CharField(blank=True, max_length=14, unique=True)),
                ('nationality', models.CharField(choices=[('EGY', 'Egypt'), ('USA', 'United States of America'), ('CAN', 'Canada'), ('UK', 'United Kingdom'), ('IN', 'India'), ('AU', 'Australia'), ('DE', 'Germany'), ('FR', 'France'), ('OT', 'Other')], default='OT', max_length=3)),
                ('subscription_type', models.CharField(choices=[('standard', 'standard'), ('VIP', 'VIP')], default='standard', max_length=20)),
                ('license_id', models.ImageField(blank=True, null=True, upload_to='')),
                ('Wallet_Balance', models.CharField(max_length=255)),
                ('Registration_Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, related_name='parking_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='parking_user_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
