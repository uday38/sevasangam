# Generated by Django 5.0.1 on 2024-01-20 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='full_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
