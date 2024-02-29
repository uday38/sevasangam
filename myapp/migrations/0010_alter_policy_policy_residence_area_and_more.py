# Generated by Django 4.2.3 on 2024-02-29 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_aadhar_bpl_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='policy_residence_area',
            field=models.CharField(choices=[('Urban', 'Urban'), ('Rural', 'Rural'), ('Both', 'Both')], max_length=50),
        ),
        migrations.AlterField(
            model_name='policy',
            name='policy_type',
            field=models.CharField(choices=[('Health', 'Health'), ('Life', 'Life'), ('Auto', 'Auto'), ('Home', 'Home'), ('Travel', 'Travel')], max_length=50),
        ),
    ]