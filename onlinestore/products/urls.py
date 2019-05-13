from django.urls import path

from .views import product_detail, product_list, manufacturer_detail, \
                   manufacturer_list

urlpatterns = [
    # Typically endpoints for APIs are like /api/products/ for example.
    # Look at /onlinestore/urls.py for the urlpath for this endpoint.
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    
    path('manufacturers/', manufacturer_list, name='manufacturer-list'),
    path('manufacturers/<int:pk>/', manufacturer_detail, name='manufacturer-detail')
]
