# Generated by Django 4.2.2 on 2023-07-01 16:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="distraction",
            name="time",
            field=models.DateTimeField(),
        ),
    ]
