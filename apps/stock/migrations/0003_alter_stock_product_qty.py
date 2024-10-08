# Generated by Django 5.0.6 on 2024-07-16 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_stock_created_by_stock_modified_by_stock_stock_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='product_qty',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]