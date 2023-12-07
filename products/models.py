from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.TextField()
    image_url = models.CharField(max_length=1000,null=True)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE , null=True)
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE , null=True)
    color = models.CharField(max_length=100, null=True)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name