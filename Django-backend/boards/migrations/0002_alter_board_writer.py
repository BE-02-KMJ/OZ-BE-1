# Generated by Django 5.0.3 on 2024-03-07 07:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("boards", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="board",
            name="writer",
            field=models.CharField(max_length=30),
        ),
    ]
