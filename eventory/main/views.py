from distutils.command.check import check
from django.shortcuts import render, HttpResponse, redirect
from registration.models import CustomUser
from django.contrib.auth.hashers import check_password


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(username=username)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect('cabinet')
            else:
                return HttpResponse('Неверный пароль')
        except CustomUser.DoesNotExist:
            return HttpResponse('Пользователь не найден')

    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')



