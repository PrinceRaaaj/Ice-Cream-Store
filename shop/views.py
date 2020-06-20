from .models import Product
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    products = Product.objects.all()
    print(products[0].product_desc)
    context = {"products" : products,}
    return render(request, "shop/index.html", context)

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    return render(request, "shop/contact.html")

def search(request):
    return render(request, "shop/search.html")

def track(request):
    return render(request, "shop/track.html")

def productView(request):
    return render(request, "shop/productView.html")

def checkout(request):
    return render(request, "shop/checkout.html")


