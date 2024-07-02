# Generated by Django 5.0.6 on 2024-06-19 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoice", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("item_name", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "quantity",
                    models.DecimalField(decimal_places=2, default=1, max_digits=6),
                ),
                (
                    "unit_price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                ("total", models.DecimalField(decimal_places=2, max_digits=6)),
                ("tva", models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                (
                    "reduction",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="item",
                        to="invoice.invoice",
                    ),
                ),
            ],
        ),
    ]
