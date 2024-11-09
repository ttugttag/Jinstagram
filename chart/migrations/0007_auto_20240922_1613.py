# Generated by Django 3.2.15 on 2024-09-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0006_auto_20240922_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samsung',
            name='Bank',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='Close_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='Finance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='Foreigner',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='Individual',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='Insurance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='Investment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='Organ',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='Other_corporations',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='Other_finance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='Other_foreiner',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='Pension_fund',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='Private_fund',
            field=models.IntegerField(default=0),
        ),
    ]