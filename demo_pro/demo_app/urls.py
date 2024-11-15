from django.urls import path
from . import views

urlpatterns=[
    path('',views.demo_login),
    path('shop_home',views.shop_home),
    path('logout',views.demo_shop_logout),
    path('add',views.add_products)
]