# Generated by Django 4.2.7 on 2023-12-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_profile_directories"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="username",
            field=models.CharField(default="username", max_length=100),
            preserve_default=False,
        ),
    ]