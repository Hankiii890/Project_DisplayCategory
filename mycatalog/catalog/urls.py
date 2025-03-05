from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.lst_category, name='list_category'),
    path('category/<int:category_id>', views.category_detail, name='category_detail'),

]