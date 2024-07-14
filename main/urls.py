from django.urls import path 
from . import views 
urlpatterns = [
    path('',views.index,name='home'),
    path('cart',views.cart,name='cart'),
    path('about',views.about,name='about'),
    path('checkout',views.checkout,name='checkout'),
    path('men',views.men,name='men'),
    path('women',views.women,name='women'),
    path('product-detail',views.product_detail,name='product-detail'),
    path('contact',views.contact,name='contact')
]