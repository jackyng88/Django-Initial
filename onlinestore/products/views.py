from django.http import JsonResponse
from .models import Product, Manufacturer


def product_list(request):
    products = Product.objects.all()
    # You can also take a slice of the objects i.e. [:30]
    data = {'products': list(products.values())}     # 'pk', 'name'
    response = JsonResponse(data)
    
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {'product': 
                    {
                    'name': product.name,
                    'manufacturer': product.manufacturer.name,
                    'description': product.description,
                    'photo': product.photo.url,
                    'price': product.price,
                    'shipping_cost': product.shipping_cost,
                    'quantity': product.quantity,
                    }
                }
        response = JsonResponse(data)
     
    except Product.DoesNotExist:   
         response = JsonResponse({
             'error': {
                 'code': 404,
                 'message': 'product not found!'
             }
         }, status=404)

    return response

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.filter(active=True)
    # Filter instead of all() to show only active manufacturers
    data = {'manufacturer': list(manufacturers.values())}     # 'pk', 'name'
    response = JsonResponse(data)
    
    return response

def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_products = manufacturer.products.all()
        # the manufacturer model has an inverse relationship provided in the
        # related_name field.
        data = {'manufacturer': 
                    {
                    'name': manufacturer.name,
                    'location': manufacturer.location,
                    'active': manufacturer.active,
                    'products': list(manufacturer_products.values())
                    }
                }
        response = JsonResponse(data)
     
    except Manufacturer.DoesNotExist:   
         response = JsonResponse({
             'error': {
                 'code': 404,
                 'message': 'manufacturer not found!'
             }
         }, status=404)

    return response



""" from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html' """

