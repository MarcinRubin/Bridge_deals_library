# Generated by Django 4.2.7 on 2023-11-19 20:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("deals", "0002_deal_visiblity"),
    ]

    operations = [
        migrations.RenameField(
            model_name="deal",
            old_name="visiblity",
            new_name="visibility",
        ),
    ]
