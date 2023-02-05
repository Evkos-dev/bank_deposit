# Generated by Django 4.1.6 on 2023-02-04 11:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10, verbose_name='Дата вклада')),
                ('periods', models.PositiveSmallIntegerField(max_length=8, verbose_name='Период вклада')),
                ('amount', models.PositiveIntegerField(max_length=16, verbose_name='Сумма вклада')),
                ('rate', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)], verbose_name='Процент по вкладу')),
            ],
        ),
    ]
