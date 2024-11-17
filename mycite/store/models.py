from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Product(models.Model):
    product_name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    have = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return f'{self.product_name}-{self.price}'

