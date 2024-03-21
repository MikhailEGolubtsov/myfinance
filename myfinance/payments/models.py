from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Currency(models.Model):
    name = models.CharField(max_length=100, verbose_name='Валюта')
    slug = models.SlugField(
        unique=True,
        max_length=3,
        verbose_name='Код'
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.TextField(verbose_name='Пользователь')
    slug = models.SlugField(
        unique=True,
        max_length=32,
        verbose_name='Имя'
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    name = models.TextField(verbose_name='Тип платежа')
    slug = models.SlugField(
        unique=True,
        max_length=32,
        verbose_name='Код'
    )
    code = models.CharField(max_length=6, verbose_name='Наименование')
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Payment(models.Model):
    sum = models.FloatField(null=False, blank=False, default=0)

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='Платеж'
    )
    payment_type = models.ForeignKey(
        PaymentType,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='Платеж'
    )
    currency= models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='Платеж'
    )
    FactOrPlanned = models.BooleanField(
        verbose_name='Фактический',
        default=True
    )
    TakeIntoReports = models.BooleanField(
        verbose_name='Учитывать в отчетах',
        default=True
    )
    payment_date = models.DateTimeField(
        verbose_name='Дата платежа',
        auto_now_add=True
    )

    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
