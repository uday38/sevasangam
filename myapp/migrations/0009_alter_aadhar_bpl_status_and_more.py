# Generated by Django 4.2.3 on 2024-02-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_aadhar_firstname_aadhar_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aadhar',
            name='bpl_status',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='aadhar',
            name='disability_status',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='aadhar',
            name='minority_status',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='policy',
            name='policy_bpl_status',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3),
        ),
        migrations.AlterField(
            model_name='policy',
            name='policy_disability_status',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='policy',
            name='policy_minority_status',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
    ]
