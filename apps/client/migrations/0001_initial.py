# Generated by Django 5.0.6 on 2024-06-13 15:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("clientId", models.CharField(blank=True, max_length=255, null=True)),
                ("contact_name", models.CharField(max_length=255)),
                ("company_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("siret", models.CharField(blank=True, max_length=255, null=True)),
                ("address", models.CharField(max_length=255)),
                ("code_postal", models.CharField(max_length=255)),
                ("ville", models.CharField(max_length=255)),
                ("pays", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="clients",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
