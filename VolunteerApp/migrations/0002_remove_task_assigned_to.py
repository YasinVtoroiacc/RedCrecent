# Generated by Django 4.1.13 on 2024-10-30 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VolunteerApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
    ]
