# Generated by Django 3.2.11 on 2022-01-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gcc", "0007_machine_mac_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="machine",
            name="mac_id",
        ),
        migrations.AlterField(
            model_name="machine",
            name="id",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
