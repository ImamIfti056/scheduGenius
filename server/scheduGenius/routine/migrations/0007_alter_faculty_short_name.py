# Generated by Django 5.1.5 on 2025-01-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("routine", "0006_faculty_short_name_alter_faculty_contact_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faculty",
            name="short_name",
            field=models.CharField(default="d", max_length=50),
        ),
    ]
