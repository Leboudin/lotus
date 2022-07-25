# Generated by Django 4.0.6 on 2022-07-24 22:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        (
            "billing",
            "0002_remove_billingplan_active_remove_billingplan_amount_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="properties",
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="event",
            name="time_created",
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("start_date", models.DateTimeField(auto_now=True, max_length=100)),
                ("end_date", models.DateTimeField(auto_now=True, max_length=100)),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("ended", "Ended")],
                        default="active",
                        max_length=6,
                    ),
                ),
                (
                    "billing_plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="billing.billingplan",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="billing.customer",
                    ),
                ),
            ],
        ),
    ]
