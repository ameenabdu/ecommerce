from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request, 'customer/customer_home.html')

def my_cart(request):
    return render(request, 'customer/my_cart.html')

def my_orders(request):
    return render(request, 'customer/my_orders.html')

def wishlist(request):
    return render(request, 'customer/wishlist.html')

def masterpage(request):
    return render(request, 'customer/masterpage.html')

def about_us(request):
    return render(request, 'customer/about_us.html')

    
