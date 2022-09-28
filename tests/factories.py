import factory.django
from factory import Faker

from ads.models import Ads
from category.models import Category
from selection.models import Selection
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = Faker("name")
    password = "test"


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = "test name"
    slug = Faker("first_name")


class AdsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ads

    name = "test"
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    price = 2000


class SelectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Selection

    name = "test"
    owner = factory.SubFactory(UserFactory)


