from django.shortcuts import render, get_object_or_404, redirect
from .models import ProductCategory, Product
from .forms import ProductCategoryForm, ProductForm


# Отображение всех категорий и товаров
def lst_category(request):
    category = ProductCategory.objects.filter(parent=None)    # Получение корневых категорий
    return render(request, 'category_list.html', {'category': category})


def category_detail(request, category_id):
    category = get_object_or_404(ProductCategory, id=category_id)
    products = category.products.all()  # Все продукты в категории (Определено в модели Product. Объект категории можно получить все связанные с ним товары через атрибут products)
    subcategories = category.children.all()    # Подкатегории. Так же обращаемся к reload_name, но в модели ProductCategory
    return render(request, 'category_detail.html',
                  {
                      'category': category,
                      'products': products,
                      'subcategories': subcategories,
                  }
                  )


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})