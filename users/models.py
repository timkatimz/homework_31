from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


def check_non_rambler_domain(value: str):
    if 'rambler.ru' in value:
        raise ValidationError("Неверное значение. Домен Rambler не поддерживается")


def check_birth_date(value):
    today_year = date.today().year
    value = today_year - value.year
    if value < 9:
        raise ValidationError("Неверное значение")


class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = 'admin', 'Администратор'
        MODERATOR = 'moderator', 'Модератор'
        MEMBER = 'member', 'Пользователь'

    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.SlugField(max_length=255)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.MEMBER)
    age = models.SmallIntegerField(null=True)
    birth_date = models.DateField(null=True, validators=[check_birth_date])
    email = models.EmailField(unique=True, validators=[check_non_rambler_domain], null=True)
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['username']

    def __str__(self):
        return self.username
