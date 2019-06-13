from django.urls import path
from . import views



app_name='shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),

    path('add/', views.product_create_view, name='add_product'),

    path('add_category/', views.category_create_view, name='add_category'),

    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),

    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
]