# Generated by Django 5.1.5 on 2025-01-20 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Classroom",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("classroom_no", models.CharField(max_length=20, unique=True)),
                ("capacity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                ("course_id", models.AutoField(primary_key=True, serialize=False)),
                ("course_no", models.CharField(max_length=20, unique=True)),
                ("course_title", models.CharField(max_length=200)),
                ("credit", models.IntegerField()),
                ("year", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Faculty",
            fields=[
                ("faculty_id", models.AutoField(primary_key=True, serialize=False)),
                ("faculty_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("contact", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Period",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name="FacultyCourse",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="routine.course"
                    ),
                ),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="routine.faculty",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MasterRoutine",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("Monday", "Monday"),
                            ("Tuesday", "Tuesday"),
                            ("Wednesday", "Wednesday"),
                            ("Thursday", "Thursday"),
                            ("Friday", "Friday"),
                            ("Saturday", "Saturday"),
                            ("Sunday", "Sunday"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "classroom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="routine.classroom",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="routine.course"
                    ),
                ),
                (
                    "faculty",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="routine.faculty",
                    ),
                ),
                (
                    "period",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="routine.period"
                    ),
                ),
            ],
        ),
    ]
