from django.db import models

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='orders', null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    products = models.ManyToManyField('products.Product')  # Use ManyToManyField for multiple products
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"