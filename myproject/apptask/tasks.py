import random
import string
import time
from .models import MyModel

from celery import shared_task
import numpy as np
from celery.decorators import task
from django.core.cache import cache
import os
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)




@shared_task
def add(x, y):
    return x + y
   #sum = task.delay(x, y, kwarg1='x', kwarg2='y')
    #task.s(arg1, arg2, kwarg1='x', kwargs2='y').apply_async(countdown=10)
    #T.apply_async(countdown=10)
    #time.sleep(10)


@shared_task
def newarr():
    multiply = []
    myarray1 = [random.randint(1, 10) for _ in range(10)]
    myarray2 = [random.randint(1, 10) for _ in range(10)]
    time.sleep(10)
    return ((f'this is a tuple 1 {myarray1}'), (f'this is a tuple 1 {myarray2}'), (f'this is  multiplication {np.multiply(myarray1, myarray2)}') )


@shared_task
def xsum(a, b):
   time.sleep(3)
   res = a+b
   logger.info(f'Add: {a} + {b} = {res}')
   return res



#@shared_task
#@def do_job(path, task_id=None):
 #   cache.set(task_id, operation_results)



@shared_task
def create_new_object():
    random_name = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    new_object = MyModel.objects.create(name=random_name)
    return new_object.name







