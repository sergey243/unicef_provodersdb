# Generated by Django 4.2.8 on 2024-01-01 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("providers", "0013_evaluation"),
    ]

    operations = [
        migrations.RemoveField(model_name="evaluation", name="service",),
        migrations.AddField(
            model_name="evaluation",
            name="services",
            field=models.ManyToManyField(
                blank=True, to="providers.service", verbose_name="services evaluated"
            ),
        ),
        migrations.RemoveField(model_name="evaluation", name="goods",),
        migrations.RemoveField(model_name="evaluation", name="works",),
        migrations.AddField(
            model_name="evaluation",
            name="goods",
            field=models.ManyToManyField(
                blank=True, to="providers.good", verbose_name="good evaluated"
            ),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="works",
            field=models.ManyToManyField(
                blank=True, to="providers.work", verbose_name="works evaluated"
            ),
        ),
    ]