# Generated by Django 5.1.5 on 2025-01-21 14:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("routine", "0003_remove_course_year_course_course_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="year",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
