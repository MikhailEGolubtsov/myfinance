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
    code = models.CharField((max_length=6, verbose_name='Наименование')
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Payment(models.Model):
    sum = models.DecimalField()
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='Платеж'
    )
    score = models.SmallIntegerField(
        verbose_name='Оценка',
        validators=(
            MinValueValidator(1),
            MaxValueValidator(10)
        ),
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )