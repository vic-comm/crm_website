# Generated by Django 5.2 on 2025-05-05 23:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leads", "0005_category_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="leads.userprofile"
            ),
        ),
    ]
