# Generated by Django 5.2 on 2025-05-05 23:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leads", "0004_category_task_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="leads.userprofile",
            ),
        ),
    ]
