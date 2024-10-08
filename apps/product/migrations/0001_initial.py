# Generated by Django 5.0.6 on 2024-06-26 13:13

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
            name="Product",
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
                ("product_id", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "product_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "product_unit_price",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "product_type",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("on_going_command", models.IntegerField(default=0)),
                ("minimun_stock", models.IntegerField(default=0)),
                ("tva", models.IntegerField(default=20)),
                ("price", models.IntegerField(default=20)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="creater_product",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="modifier_product",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stock",
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
                ("product_qty", models.IntegerField()),
                (
                    "product_site",
                    models.CharField(
                        choices=[
                            ("LIL", "Lille"),
                            ("VIO", "Violet"),
                            ("VIA", "Viaduc"),
                            ("LOU", "Lourmel"),
                        ],
                        max_length=10,
                    ),
                ),
                ("stock_DDM", models.DateField(null=True)),
                ("modified_at", models.DateField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="creator_stocks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="modifier_stocks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stocks",
                        to="product.product",
                    ),
                ),
            ],
        ),
    ]
