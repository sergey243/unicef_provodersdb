# Generated by Django 4.2.8 on 2023-12-19 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("providers", "0005_remove_good_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="provider",
            old_name="coveredCitiesGoods",
            new_name="covered_cities_Goods",
        ),
        migrations.RenameField(
            model_name="provider",
            old_name="coveredCitiesServices",
            new_name="covered_cities_services",
        ),
        migrations.RenameField(
            model_name="provider",
            old_name="coveredCitiesWorks",
            new_name="covered_cities_works",
        ),
    ]