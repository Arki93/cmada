# Generated by Django 5.0.6 on 2024-06-20 09:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("invoice", "0008_alter_invoice_total_ht_alter_invoice_total_tva"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="invoice",
            name="team",
        ),
    ]