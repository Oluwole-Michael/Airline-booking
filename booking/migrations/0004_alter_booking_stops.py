# Generated by Django 5.0 on 2024-01-05 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_remove_hotelbooking_check_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='stops',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
