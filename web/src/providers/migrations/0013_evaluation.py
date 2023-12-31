# Generated by Django 4.2.8 on 2024-01-01 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("providers", "0012_alter_provider_ungm_number_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Evaluation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(editable=False)),
                ("modified_at", models.DateTimeField(editable=False)),
                ("lta", models.CharField(max_length=50, verbose_name="LTA number")),
                (
                    "po_number",
                    models.CharField(max_length=50, verbose_name="PO number"),
                ),
                (
                    "po_amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=20, verbose_name="PO amount"
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="description",
                    ),
                ),
                (
                    "fiability",
                    models.IntegerField(
                        choices=[
                            (1, "poor"),
                            (2, "not satisfying"),
                            (3, "acceptable"),
                            (4, "good"),
                            (5, "excelent"),
                        ],
                        verbose_name="fiability",
                    ),
                ),
                (
                    "timing",
                    models.IntegerField(
                        choices=[
                            (1, "poor"),
                            (2, "not satisfying"),
                            (3, "acceptable"),
                            (4, "good"),
                            (5, "excelent"),
                        ],
                        verbose_name="timing",
                    ),
                ),
                (
                    "best_value",
                    models.IntegerField(
                        choices=[
                            (1, "poor"),
                            (2, "not satisfying"),
                            (3, "acceptable"),
                            (4, "good"),
                            (5, "excelent"),
                        ],
                        verbose_name="quality-price report",
                    ),
                ),
                (
                    "tech_specification",
                    models.IntegerField(
                        choices=[
                            (1, "poor"),
                            (2, "not satisfying"),
                            (3, "acceptable"),
                            (4, "good"),
                            (5, "excelent"),
                        ],
                        verbose_name="technical specifications",
                    ),
                ),
                (
                    "comment",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="comment"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="ecreator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "goods",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="providers.good",
                        verbose_name="goods",
                    ),
                ),
                (
                    "last_modify_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="emodifier",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="provider",
                        to="providers.provider",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="providers.service",
                        verbose_name="services",
                    ),
                ),
                (
                    "works",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="providers.work",
                        verbose_name="works",
                    ),
                ),
            ],
            options={
                "db_table": "evaluations",
                "ordering": ["provider"],
                "get_latest_by": ["created_at", "modified_at"],
                "default_related_name": "evaluations",
            },
        ),
    ]
