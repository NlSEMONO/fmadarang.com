from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Inventory)
admin.site.register(ShopLocation)
admin.site.register(ProductLister)
admin.site.register(ProductTracker)
admin.site.register(Order)