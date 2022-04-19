import datetime

from django.test import TestCase

from .factories import PantryFactory, PersonFactory, ItemFactory
from .models import Pantry, Person, Item
from .sevices import receive_restock_post


class PantryRestockTest(TestCase):
    item: Item
    pantry: Pantry
    stocker: Person

    def setUp(self) -> None:
        self.item = ItemFactory.create()
        self.pantry = PantryFactory.create()
        self.stocker = PersonFactory.create()

    def test_valid_form_submission(self):
        restock = receive_restock_post(
            cleanliness_score=5,
            comment='All good here',
            fullness_on_arrival=4,
            fullness_on_departure=6,
            needs=['Socks', self.item.name],
            pantry=self.pantry.id,
            photo=None,
            restock_date=datetime.date(2022, 4, 18),
            reporter_email=self.stocker.email,
            reporter_name='Stocker Extraordinaire',
            submitted_at=datetime.datetime(2022, 4, 18, 12, 34, 56),
        )

        self.assertEqual('Stocker Extraordinaire', restock.reporter.name)
        self.assertIn(self.item, restock.needs.all())
        self.assertIn(Item.objects.get(name='Socks'), restock.needs.all())
