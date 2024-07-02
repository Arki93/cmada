# Generated by Django 5.0.6 on 2024-06-20 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoice", "0015_remove_invoice_team"),
        ("team", "0003_alter_team_rcs_alter_team_siret_alter_team_tva_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="factures",
                to="team.team",
            ),
        ),
    ]
