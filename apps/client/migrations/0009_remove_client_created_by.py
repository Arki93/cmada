# Generated by Django 5.0.6 on 2024-10-08 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_alter_client_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='created_by',
        ),
    ]