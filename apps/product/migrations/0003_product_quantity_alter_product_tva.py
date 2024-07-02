# Generated by Django 5.0.6 on 2024-06-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_remove_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=6, null=True
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="tva",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=6, null=True
            ),
        ),
    ]