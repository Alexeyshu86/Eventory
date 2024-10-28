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
                request.session['errors_incorrect'] = 'Почта или пароль не верны'
                return redirect('home')
        except CustomUser.DoesNotExist:
            request.session['errors_incorrect'] = 'Почта или пароль не верны'
            return redirect('home')

    errors_incorrect = request.session.pop('errors_incorrect', None)
    return render(request, 'main/index.html', {'errors_incorrect': errors_incorrect})


def about(request):
    return render(request, 'main/about.html')



