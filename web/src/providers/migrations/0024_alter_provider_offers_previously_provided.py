# Generated by Django 4.2.8 on 2024-03-06 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0023_alter_evaluation_best_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='offers_previously_provided',
            field=models.TextField(blank=True, help_text='ordres received from Unicef, other united state organizations, bilateral coperation agencies or gorvenemental agencies fro the pqst three year', max_length=2500, null=True, verbose_name='offers previously provided'),
        ),
    ]
