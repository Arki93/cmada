# Generated by Django 5.0.6 on 2024-10-08 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_remove_productstock_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productstock',
            name='created_by',
        ),
    ]
