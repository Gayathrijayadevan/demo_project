from django.urls import path
from . import views

urlpatterns=[
    path('',views.demo_login),

    #---------------admin-------------------
    path('shop_home',views.shop_home),
    path('logout',views.demo_shop_logout),
    path('add',views.add_products),
    path('edit_product/<pid>',views.edit_product),
    path('delete_product/<pid>',views.delete_product),
    path('view_bookings',views.view_bookings),

    #-----------------------user-----------------------
    path('register',views.register),
    path('user_home',views.user_home),
    path('product_dtl/<pid>',views.pro_dtl),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('view_cart',views.view_cart),
    path('qty_in/<cid>',views.qty_in),
    path('qty_dec/<cid>',views.qty_dec),
    path('cart_pro_buy/<cid>',views.cart_pro_buy),
    path('bookings',views.bookings),
    path('pro_buy/<pid>',views.pro_buy),
]