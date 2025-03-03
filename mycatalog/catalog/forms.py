from django import forms
from .models import ProductCategory, Product


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name', 'parent']


class ProductForm(forms.ModelForm):
    class Meta:
        models = Product
        fields = ['name', 'description', 'category', 'price', 'created_at']
