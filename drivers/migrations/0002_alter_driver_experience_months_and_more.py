# Generated by Django 4.2.14 on 2024-07-24 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='experience_months',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='driver',
            name='experience_years',
            field=models.PositiveIntegerField(),
        ),
    ]
