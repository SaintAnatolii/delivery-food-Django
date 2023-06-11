from django.contrib import admin
from .models import Restaurant, Product, Cart
# Register your models here.


admin.site.register(Product)
admin.site.register(Restaurant)
admin.site.register(Cart)