from django.shortcuts import render
from .models import Interest


def index(request):
    record = Interest(interest="IT")
    record.save()
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')
