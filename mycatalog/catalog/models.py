from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class ProductCategory(MPTTModel):
    """Модель категории продуктов"""
    name = models.CharField(max_length=255)    # Имя самой категории
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        """Сортировка категории будет происходить по имени"""
        order_insertion_by = ['name']


class Product(models.Model):
    """Каждый продукт будет связан с одной категорией"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = TreeForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
