# Generated by Django 5.0.6 on 2024-06-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("client", "0002_rename_clientid_client_client_reference"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="number",
            field=models.CharField(default=78979878, max_length=255),
            preserve_default=False,
        ),
    ]