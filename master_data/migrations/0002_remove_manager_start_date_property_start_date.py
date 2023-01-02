# Generated by Django 4.1.4 on 2023-01-02 14:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='start_date',
        ),
        migrations.AddField(
            model_name='property',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
