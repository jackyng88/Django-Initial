from django.urls import path

from .views import product_detail, product_list

urlpatterns = [
    # Typically endpoints for APIs are like /api/products/ for example.
    # Look at /onlinestore/urls.py for the urlpath for this endpoint.
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
]
