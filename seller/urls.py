from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [                                       
    path('home',views.seller_home, name='seller-home'),
    path('add_product',views.add_product, name='add-product')
]
