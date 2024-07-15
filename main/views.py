from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{
        'products':products
    })
def cart(request):
    return render(request,'cart.html')


def about(request):
    return render(request,'about.html')
def checkout(request):
    return render(request,'checkout.html')
def men(request):
    products = Product.objects.filter(gender = 'm')
    return render(request,'men.html',{
        'products':products
    })
def women(request):
    products = Product.objects.filter(gender = 'f')
    return render(request,'women.html',{
        'products':products
    })
def product_detail(request,pk):
    product = Product.objects.get(pk = pk)
    return render(request,'product-detail.html',{
        'product': product
    })
def contact(request):
    return render(request,'contact.html')