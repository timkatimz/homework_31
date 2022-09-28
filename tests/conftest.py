from pytest_factoryboy import register

from tests.factories import UserFactory, AdsFactory, CategoryFactory, SelectionFactory

pytest_plugins = "tests.fixtures"

register(UserFactory)
register(AdsFactory)
register(CategoryFactory)
register(SelectionFactory)
