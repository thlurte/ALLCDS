# Generated by Django 4.2.5 on 2023-09-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allcds', '0004_record_is_true'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='age',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]