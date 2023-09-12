# Generated by Django 4.2.3 on 2023-09-12 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("github", models.URLField(blank=True)),
                ("linkedin", models.URLField(blank=True)),
                ("bio", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField(max_length=500)),
                ("github_url", models.URLField(blank=True)),
                ("keyword", models.CharField(max_length=50)),
                ("key_skill", models.CharField(max_length=50)),
                (
                    "profile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project",
                        to="projects.profile",
                    ),
                ),
            ],
        ),
    ]
