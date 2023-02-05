from django.db import models
from django.core.validators import (MinValueValidator, MaxValueValidator,
                                    RegexValidator)


class Deposit(models.Model):
    date = models.CharField(
        verbose_name='Дата вклада',
        max_length=10,
        validators=[
            RegexValidator(regex=r'\d\d\.\d\d\.\d{4}')
        ]
    )
    periods = models.PositiveSmallIntegerField(
        verbose_name='Период вклада в месяцах'
    )
    amount = models.PositiveIntegerField(verbose_name='Сумма вклада')
    rate = models.FloatField(
        verbose_name='Процент по вкладу',
        validators=[
            MinValueValidator(1), MaxValueValidator(8)
        ]
    )
