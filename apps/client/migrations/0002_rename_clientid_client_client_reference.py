# Generated by Django 5.0.6 on 2024-06-13 19:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("client", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="client",
            old_name="clientId",
            new_name="client_reference",
        ),
    ]
