from django.db import models
from user.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    time_of_delivery = models.CharField(max_length=100)
    stars = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.IntegerField()
    kitchen = models.CharField(max_length=100)
    image = models.ImageField(upload_to='restaurant_images', blank=False, null=False)

    def __str__(self): return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    image = models.ImageField(upload_to='restaurant_images', blank=False, null=False)
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)

    def __str__(self): return self.name

class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)

    def sum(self): return self.amount * self.product.price
    
    def total_sum(self):
        carts = Cart.objects.filter(user=self.user)
        return sum(cart.sum() for cart in carts)

    def __str__(self): return f'Продукт: {self.product.name}'
