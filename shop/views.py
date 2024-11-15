from django.shortcuts import render
from .models import Product,Order

# Create your views here.
def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/сatalog.html', {'products': products}) 

def orders(request):
    orders = Order.objects.all()
    return render(request, 'shop/orders.html',{'orders': orders})


def create_order(request, product_id):
    if request.method == "POST":
        u_address = request.POST["address"]
        u_email = request.POST["email"]
        u_phone = request.POST["phone"]
        u_koment = request.POST["koment"]
        u_count = request.POST["count"]
        Order.objects.create(
            product = Product.objects.get(id=product_id),
            address = u_address,
            phone = u_phone,
            email = u_email,
            koment = u_koment,
            count = u_count,
        )
    return render(request, 'shop/create_order.html')


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})



