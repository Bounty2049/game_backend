# Generated by Django 5.0.3 on 2024-03-26 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
