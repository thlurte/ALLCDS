# Generated by Django 4.2.5 on 2023-09-25 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allcds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='clinical_results',
            field=models.FileField(blank=True, null=True, upload_to='clinical_results/'),
        ),
        migrations.AddField(
            model_name='record',
            name='genatic_information',
            field=models.FileField(blank=True, null=True, upload_to='genatic_information/'),
        ),
        migrations.AddField(
            model_name='record',
            name='lab_results',
            field=models.FileField(blank=True, null=True, upload_to='lab_results/'),
        ),
        migrations.AddField(
            model_name='record',
            name='medical_history',
            field=models.FileField(blank=True, null=True, upload_to='medical_history/'),
        ),
        migrations.AddField(
            model_name='record',
            name='radiology_results',
            field=models.FileField(blank=True, null=True, upload_to='radiology_results/'),
        ),
    ]
