# Generated by Django 4.2.7 on 2023-11-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Poll",
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
                ("title", models.CharField(max_length=128)),
                ("text", models.TextField(blank=True)),
                ("score", models.IntegerField(default=0)),
            ],
        ),
    ]
