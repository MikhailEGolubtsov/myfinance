from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Currency(models.Model):
    name = models.TextField()
    slug = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.TextField()
    slug = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name
