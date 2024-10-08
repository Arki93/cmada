# Generated by Django 5.0.6 on 2024-07-16 12:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_alter_stock_product_qty'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='modified_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='entry_status',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='product_qty',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='product_site',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='stock_DDM',
        ),
        migrations.AddField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='create_product', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='minimun_stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modify_product', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='tva',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_stock_id', models.CharField(blank=True, max_length=100, null=True)),
                ('product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('product_qty', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('product_site', models.CharField(choices=[('LIL', 'Lille'), ('VIO', 'Violet'), ('VIA', 'Viaduc'), ('LOU', 'Lourmel')], max_length=10)),
                ('stock_DDM', models.DateField(null=True)),
                ('entry_status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_product', to='stock.product')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='stock.stock')),
            ],
        ),
    ]
