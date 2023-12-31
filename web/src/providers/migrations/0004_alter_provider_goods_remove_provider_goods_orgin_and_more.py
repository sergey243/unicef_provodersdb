# Generated by Django 4.2.8 on 2023-12-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("providers", "0003_alter_good_last_modify_by_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="provider",
            name="goods",
            field=models.ManyToManyField(
                through="providers.GoodsProvided",
                to="providers.good",
                verbose_name="good provided",
            ),
        ),
        migrations.RemoveField(model_name="provider", name="goods_orgin",),
        migrations.AlterField(
            model_name="provider",
            name="services",
            field=models.ManyToManyField(
                through="providers.ServicesProvided",
                to="providers.service",
                verbose_name="services provided",
            ),
        ),
        migrations.AlterField(
            model_name="provider",
            name="works",
            field=models.ManyToManyField(
                through="providers.WorkExecuted",
                to="providers.work",
                verbose_name="works executed",
            ),
        ),
        migrations.AddField(
            model_name="provider",
            name="goods_orgin",
            field=models.CharField(
                blank=True, max_length=250, null=True, verbose_name="origin of goods"
            ),
        ),
    ]
