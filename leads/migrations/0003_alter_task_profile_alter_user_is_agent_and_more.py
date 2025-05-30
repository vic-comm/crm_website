# Generated by Django 5.2 on 2025-05-05 22:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leads", "0002_alter_task_employee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="leads.userprofile",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_agent",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_organisor",
            field=models.BooleanField(default=False),
        ),
    ]
