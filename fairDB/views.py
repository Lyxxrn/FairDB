from django.shortcuts import render, get_object_or_404
from .models import Product


# frontend views

def index(request):
    return render(request, 'index.html')

def product_detail(request, barcode):
    product = get_object_or_404(Product, barcode=barcode)
    context = {
        'product': product,
        'gold_stars': product.gold_stars(),
        'gray_stars': product.gray_stars(),
    }
    return render(request, 'product.html', context)