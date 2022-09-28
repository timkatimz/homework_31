from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


from category.models import Category
from users.models import User


def check_name(value: str):
    if len(value) < 10:
        raise ValidationError("Значение поле не может быть менее 10 символов")



class Ads(models.Model):
    name = models.CharField(max_length=100, null=False, validators=[check_name])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='ads/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name
