from django.shortcuts import render, HttpResponse, redirect
from registration.models import CustomUser
from django.contrib.auth.hashers import check_password


def index(request):
    errors_incorrect = None
    if request.method == 'GET':
        return render(request, 'main/index.html',
                      {'errors_incorrect': errors_incorrect})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(username=username)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect('cabinet')
            else:
                errors_incorrect = 'Почта или пароль не верны'
                return render(request, 'main/index.html',
                              {'errors_incorrect': errors_incorrect})
        except CustomUser.DoesNotExist:
            errors_incorrect = 'Почта или пароль не верны'
            return render(request, 'main/index.html',
                          {'errors_incorrect': errors_incorrect})

    # return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')



