import factory
import factory.django as django_factory
import factory.fuzzy
from . import models


class ItemFactory(django_factory.DjangoModelFactory):
    class Meta:
        model = models.Item

    name = factory.fuzzy.FuzzyChoice(['Apples', 'Bananas', 'Cherries', 'Doughnuts', 'Elephant Ears'])


class PersonFactory(django_factory.DjangoModelFactory):
    class Meta:
        model = models.Person

    email = factory.Faker('email')
    name = factory.Faker('name')


class PantryFactory(django_factory.DjangoModelFactory):
    class Meta:
        model = models.Pantry

    address = factory.Faker('address')
    deplete_pct_per_day = 0.2
    description = 'At the Bettie Page/Divine House'
    # features = []
    host = factory.SubFactory(PersonFactory)
    overflow_dropoff = 'Somewhere under I-5'
    size = 'medium'
    slug = 'bettie-page-divine'
    type = models.Pantry.PantryType.PANTRY
