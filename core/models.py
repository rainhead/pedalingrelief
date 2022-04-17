from django.db import models


class EstimatedPantryStatus(models.Model):
    class Meta:
        # view defined in migrations
        db_table = 'estimated_pantry_status'
        managed = False

    est_pct_full = models.FloatField()
    last_pct_full = models.FloatField(null=True)
    last_restock_date = models.DateField(null=True)
    pantry = models.ForeignKey('Pantry', on_delete=models.CASCADE)


class Feature(models.Model):
    """Physical feature or aspect of pantry"""
    name = models.CharField(max_length=50)


class FoodBank(models.Model):
    address = models.TextField(max_length=500)
    contact_person = models.ForeignKey('Person', on_delete=models.RESTRICT)
    description = models.TextField(max_length=500, null=True)
    # location = models.PointField(geography=True)
    name = models.CharField(max_length=50)


class Item(models.Model):
    """A type of goods that can be stocked at a pantry"""
    name = models.CharField(max_length=50)


class Pantry(models.Model):
    """A physical container for goods"""

    class PantrySize(models.TextChoices):
        SMALL = 'small'
        MEDIUM = 'medium'
        LARGE = 'large'

    class PantryType(models.TextChoices):
        FRIDGE = 'fridge'
        PANTRY = 'pantry'

    address = models.TextField(max_length=500)
    # delivery_area = models.PolygonField()
    deplete_pct_per_day = models.FloatField()
    description = models.TextField(max_length=500)
    features = models.ManyToManyField('Feature')
    host = models.ForeignKey('Person', on_delete=models.RESTRICT)
    # location = models.PointField(geography=True)
    overflow_dropoff = models.TextField(
        max_length=500,
        help_text="Where to drop off items that don't fit in the pantry"
    )
    size = models.CharField(max_length=20, choices=PantrySize.choices)
    slug = models.SlugField(max_length=50, db_index=True)
    type = models.TextField(max_length=20, choices=PantryType.choices, default=PantryType.PANTRY)


class Person(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)


class Restock(models.Model):
    """An observation of a pantry before and after restocking by a particular person on a particular date"""

    class Meta:
        get_latest_by = 'restock_date'
        # Ideally only one report per pantry per day, but we can't guarantee this.
        indexes = [
            models.Index(fields=['pantry', 'restock_date'])
        ]

    cleanliness_pct = models.FloatField()
    needs = models.ManyToManyField('Item')
    pantry = models.ForeignKey('Pantry', on_delete=models.CASCADE)
    pct_full_on_arrival = models.FloatField()
    pct_full_on_departure = models.FloatField()
    photo = models.URLField(max_length=500, null=True)
    restock_date = models.DateField(db_index=True)
    reporter = models.ForeignKey('Person', db_index=True, null=True, on_delete=models.SET_NULL)
    reporter_name = models.CharField(max_length=50)
    submitted_at = models.DateTimeField(auto_now_add=True)


class DeliveryRoute(models.Model):
    """A route connecting some set of pantries on a particular day"""
    class Meta:
        get_latest_by = 'date'
        unique_together = (('food_bank', 'date', 'name'),)

    date = models.DateField()
    food_bank = models.ForeignKey('FoodBank', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    pantries = models.ManyToManyField('Pantry')

