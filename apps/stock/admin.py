from django.contrib import admin
from .models import ProductStock, Stock, ProductStockArchive

admin.site.register(ProductStock)
admin.site.register(Stock)
admin.site.register(ProductStockArchive)

