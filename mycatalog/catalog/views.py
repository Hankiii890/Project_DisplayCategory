from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductCategory, Product
from .forms import ProductCategoryForm, ProductForm


# Отображение всех категорий и товаров
def lst_category(request):
    categories = ProductCategory.objects.all()
    return render(request, 'category_list.html',{'categories': categories})
