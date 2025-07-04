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


class CurrencyType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тип валюты')
    slug = models.SlugField(
        unique=True,
        max_length=10,
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
        verbose_name='Кто'
    )
    payment_type = models.ForeignKey(
        PaymentType,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='Тип платежа'
    )
    currency= models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='Валюта'
    )
    currency_type= models.ForeignKey(
        CurrencyType,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='Тип оплаты'
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
        auto_now_add=False
    )

    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'Платеж',
        verbose_name_plural = 'Платежи',
        ordering = ('-payment_date', )

    def __str__(self):
        return self.description[:15]
