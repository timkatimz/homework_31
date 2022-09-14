from django.db import models

from ads.models import Ads
from users.models import User


class Selection(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ads)
