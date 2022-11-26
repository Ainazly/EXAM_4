from django.contrib import admin
from .models import Product, Supply, Store, Buy

admin.site.register(Buy)
admin.site.register(Product)
admin.site.register(Supply)
admin.site.register(Store)

