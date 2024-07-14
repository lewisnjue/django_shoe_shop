from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def cart(request):
    return render(request,'cart.html')


def about(request):
    return render(request,'about.html')
def checkout(request):
    return render(request,'checkout.html')
def men(request):
    return render(request,'men.html')
def women(request):
    return render(request,'women.html')
def product_detail(request):
    return render(request,'product-detail.html')
def contact(request):
    return render(request,'contact.html')