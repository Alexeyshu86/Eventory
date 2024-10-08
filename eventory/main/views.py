from django.shortcuts import render
from .models import Users


def index(request):
    user = Users.objects.create(
        last_name='Ivanov',
        first_name='Ivan',
        phone='+79538794883',
        email='alexeyshu86@mail.ru',
        password='123'
    )

    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


