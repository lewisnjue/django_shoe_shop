from django.urls import path 
from . import views 
from .models import Product
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='home'),
    path('cart',views.cart,name='cart'),
    path('about',views.about,name='about'),
    path('checkout',views.checkout,name='checkout'),
    path('men',views.men,name='men'),
    path('women',views.women,name='women'),
    path('product-detail/<int:pk>',views.product_detail,name='product-detail'),
    path('contact',views.contact,name='contact')
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
