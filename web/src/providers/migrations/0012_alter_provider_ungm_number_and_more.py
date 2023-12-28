# Generated by Django 4.2.8 on 2023-12-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("providers", "0011_alter_workexecuted_table_comment_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="provider",
            name="ungm_number",
            field=models.CharField(
                blank=True, max_length=150, null=True, verbose_name="UNGM number"
            ),
        ),
        migrations.AlterField(
            model_name="provider",
            name="unicef_vendor_number",
            field=models.CharField(
                blank=True, max_length=150, null=True, verbose_name="unicef vendo ID"
            ),
        ),
    ]