# from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Product
from api.models import Category
from django.shortcuts import get_object_or_404

def product_list(request):
    products = Product.objects.all()
    products_json = [p.to_json() for p in products] 
    return JsonResponse(products_json, safe = False)

def category_list(request):
    categories = Category.objects.all()
    categories_json = [c.to_json() for c in categories]
    return JsonResponse(categories_json, safe=False)

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    data = category.to_json()
    return JsonResponse(data)

def product_detail(request,id):
    product = get_object_or_404(Product, id=id)
    data = product.to_json()
    return JsonResponse(data)

def category_products(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.product_set.all()
    data = [p.to_json() for p in products]
    return JsonResponse(data,safe = False)

