from django.shortcuts import render
from registration.models import CustomUser


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
