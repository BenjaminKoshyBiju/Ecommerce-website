from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='home'),
    path('shop',views.shop,name='shop'),
    path('contact',views.contact,name='contact'),
    path('checkout',views.checkout,name='checkout'),
    path('detail/<int:table1_id>/',views.detail,name='detail'),
    path('detail/<int:table1_id>/cart.html',views.cart,name='cart'),
     
]