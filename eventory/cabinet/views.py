from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from registration.models import CustomUser
import logging

@login_required
def cabinet(request):
    user = CustomUser.objects.get(id=request.session.get('user_id'))
    context = {
        'user': user,
    }

    return render(request, 'cabinet/cabinet.html', context)

def change_data(request):
    user = CustomUser.objects.get(id=request.session.get('user_id'))
    context = {
        'user': user,
    }

    return render(request, 'cabinet/change_data.html', context)
