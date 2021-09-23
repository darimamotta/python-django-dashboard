from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Product, Order
from .forms import ProductForm, OrderForm

# Create your views here.
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    if request.method =='POST':
       form = OrderForm(request.POST)
    else:
       form = OrderForm()
    context = {'orders': orders,
                'form': form,
               'products': products,
               }

    return render(request, 'dashboard/index.html', context)


def staff(request):
  workers = User.objects.all()
  context = {
            'workers': workers,
            }
  return render(request, 'dashboard/staff.html', context)

def staff_detail(request):
    return render(request, 'dashboard/staff_detail.html')

def product(request):
    #items = Product.objects.raw('SELECT * FROM dashboard_product')
    items = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dashboard-product')

    else:
        form = ProductForm()
        context = {
                    'items': items,
                    'form': form,
                  }
        return render(request, 'dashboard/product.html', context)

def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')

    else:
        form = ProductForm(instance=item)
        context = {'form': form }
        return render(request, 'dashboard/product_update.html', context)

def order(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'dashboard/order.html', context)

def profile(request):
    return render(request, 'dashboard/profile.html')
