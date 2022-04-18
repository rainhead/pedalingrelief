from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Feature)
admin.site.register(models.FoodBank)
admin.site.register(models.Item)
admin.site.register(models.Pantry)
admin.site.register(models.Person)
admin.site.register(models.Restock)
admin.site.register(models.DeliveryRoute)
