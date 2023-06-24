from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [                                       
    path('home',views.customer_home, name='c-home'),
    path('cart', views.my_cart, name = 'my-cart'),
    path('my-orders',views.my_orders, name = 'my-orders'),
    path('wishlist', views.wishlist, name = 'wishlist'),
    path('masterpage', views.masterpage),
    path('about_us', views.about_us)
]