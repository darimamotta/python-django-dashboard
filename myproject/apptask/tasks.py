import random
import string

from .models import MyModel
from celery import shared_task



@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def create_new_object():
    random_name = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    new_object = MyModel.objects.create(name=random_name)
    return new_object.name







