from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Currency(models.Model):
    name = models.TextField()
    slug = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.TextField()
    slug = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class PaymentType(models.Model):
    name = models.TextField()
    slug = models.TextField()
    code = models.TextField()
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