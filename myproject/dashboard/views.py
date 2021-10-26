from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Product, Order,Result
from .forms import ProductForm, OrderForm,ResultForm
from apptask.tasks import xsum
from celery.result import AsyncResult
from celery.decorators import task
from django.core.cache import cache
import hashlib

from rest_framework.views import APIView
from rest_framework.response import Response


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
    items = Product.objects.get(id=pk)
    if request.method == 'POST':
        items.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

def product_update(request, pk):
    items = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=items)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=items)
        context = {'form': form }
        return render(request, 'dashboard/product_update.html', context)

def order(request):
    orders = Order.objects.all()
    context = {
        'orders': orders, }
    #orders = cache.get('orders')
    #cache.set('orders', orders, 60)
    return render(request, 'dashboard/order.html', context)


def profile(request):
    return render(request, 'dashboard/profile.html')





def add1(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    res = xsum(a, b)
    idkey = str(res)
    id = hashlib.sha512()
    id.update(idkey.encode('utf-8'))
    id = id.hexdigest()
    id = str(id)
    ls = Result.objects.get(id=id)

    if ls in Result.id():
           ls = Result.objects.get(id=id)
           return render(request, 'dashboard/result.html', {'id': id, 'a': ls.a, 'b': ls.b, 'result': ls.res})
    else:
        form = ResultForm()
        context = {'id': id, 'a': a, 'b': b, 'result': res}
        form.save()
    #return render(request, 'dashboard/result.html',{'id':id, 'a':a, 'b':b, 'result':res })
        return render(request, 'dashboard/result.html', context)


    if request.method == 'GET':
          form = ResultForm(request.GET)
          a= a
          b=b

          context  = {'id': id, 'a': a,'b': b, 'result': res}
          form.save()
          return render(request, 'dashboard/resultlist.html', context)

    else:
        form = ResultForm()
        return render(request, 'dashboard/resultlist.html', {'form': form})

def add(request):
    #form = ResultForm(request.GET)
    a = int(request.GET['a'])
    Result.a =a
    b = int(request.GET['b'])
    Result.b =b
    #res = a + b
    #res = xsum.apply_async((a, b), expires=3)
    res = xsum(a, b)
    Result.res=res
    idkey = str(res)
    id = hashlib.sha512()
    id.update(idkey.encode('utf-8'))
    id=id.hexdigest()
    id=str(id)
    #return render(request,'dashboard/resultlist.html',{form:'form'})


    return render(request, 'dashboard/result.html', {'id': id, 'a': a, 'b': b, 'result': res })


def result_add(request):
    result_list = Result.objects.all()
    #result = Result.objects.all()
    Result.a = int(request.GET['a'])
    Result.b = int(request.GET['b'])
    Result.res = xsum(a, b)
    idkey = str(res)
    idhash = hashlib.sha512()
    idhash.update(idkey.encode('utf-8'))
    Result.id = idhash.hexdigest()
    Result.res.save()
    #mytask_id = xsum.AsyncResult(a.task_id).get()
    #if request.method =='GET':
     # form = ResultForm(request.GET)
    #else:
       #form = ResultForm()
       #context = {
                #'id': id,
              # 'a': a,
               #'b': b,
              #  'result': res,
               #}
   # return render(request, 'dashboard/result.html', context)


    #result = AsyncResult('xsum.apply_async(args=[a,b], countdown=3)
    #return render(request, 'dashboard/result.html', {'id': id, 'a': a, 'b': b, 'result': res,  })
    return HttpResponse("<h1> Xsum of %s +  %s  is  %s </h1>" % ( Result.a, Result.b, Result.res))


def result_list(request):
    result_list= Result.objects.all()
    #context= {'id': id, 'a': a, 'b': b, 'res': res }
    return render(request,'dashboard/resultlist.html', {'result_list':result_list})
def result_list_id(response,id):
 ls = Result.objects.get(id=id)
 return HttpResponse("<h1> Xsum of %s +  %s  is  %s </h1>" % ( ls.a, ls.b, ls.res))
def result_add1(request):
    results = Result.objects.all()
    if request.method == 'GET':
        form = ResultForm(request.GET, instance=results)
        if form.is_valid():
            form.save()
            return redirect('dashboard/result.html')
    else:
        form = ResultForm(instance=results)
        context = {'form': form }
        return render(request, 'dashboard/result.html', context)
def get(self, request):
    form =ResultForm()
    return render(request, self.dashboard-result, {'form':form })

def result(self, request):
    form = ResultForm(request.GET)

    if form.is_valid():
        form.save()
        Result.a = int(request.GET['a'])
        Result.a.save()
        Result.b = int(request.GET['b'])
        result.b.save()
        res = xsum(a, b)
        res.save()
        idkey = str(res)
        idhash = hashlib.sha512()
        idhash.update(idkey.encode('utf-8'))
        Result.id = idhash.hexdigest()
        Result.id.save()
        #task_id = xsum.AsyncResult(a.task_id).get()
        #newres = res.task_id
        #res = xsum.delay(a, b)
    return render(request, 'dashboard/result.html', {'id': id, 'a': a, 'b': b, 'result': res,})
    #return render(request, self.dashboard-result, args)

def resultlist(response,id):
 ls = Result.objects.get(id=id)
 return HttpResponse("<h1> Xsum of %s +  %s  is  %s </h1>" % ( ls.a, ls.b, ls.res))

class TaskSetter(APIView):
    def get(self, request, format=None):
        a = int(request.GET['a'])
        b = int(request.GET['b'])

        res = xsum(a, b)
        id = request.GET.get('task_id')
        #idkey = str(res)
        #idhash = hashlib.sha512()
        #idhash.update(idkey.encode('utf-8'))
        # res = xsum.delay(8,5)
        return Response(res)


#class TaskGetter(APIView):
  #def get(self, request, format = None):
 #res = xsum(a, b)
 #task_id = request.GET.get('task_id')
   #if task_id:
      # res= AsyncResult(task_id)
       #return Response (res.task_id)

     # return Response('No id was provided')

