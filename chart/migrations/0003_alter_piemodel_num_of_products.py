# Generated by Django 3.2.15 on 2024-09-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0002_areamodel_barmodel_piemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piemodel',
            name='num_of_products',
            field=models.FloatField(),
        ),
    ]
