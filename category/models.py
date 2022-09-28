from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


def MinSlugCharacters(value):
    if len(value) < 5:
        raise ValidationError("Поле slug не может быть короче 5 символов")


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=10, unique=True, validators=[MinSlugCharacters])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
