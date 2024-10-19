from django.shortcuts import render, HttpResponse, redirect
from .models import CustomUser, Interest


def user_registration(request):

    error_passw_repeat = None
    interest_list = Interest.objects.all()

    if request.method == 'POST':
        t_password = request.POST.get('password')
        t_password_repeat = request.POST.get('password_repeat')
        if t_password_repeat != t_password:
            error_passw_repeat = 'Пароли не совпадают.'
            return render(request, 'registration/user_regs.html',
                          {'interest_list': interest_list, 'error_passw_repeat': error_passw_repeat})
        try:
            user = CustomUser.objects.create_user(
                username=request.POST.get('email'),
                email=request.POST.get('email'),
                password=t_password,
                first_name=request.POST.get('name'),
                last_name=request.POST.get('surname'),
                phone=request.POST.get('phone'),
                interests=request.POST.getlist('tags[]')
            )
            return redirect('succ_reg')
        except Exception as e:
            return HttpResponse(f'Ошибка при создании пользователя: {str(e)}')
    else:
        return render(request, 'registration/user_regs.html',
                      {'interest_list': interest_list, 'error_passw_repeat': error_passw_repeat})

def succ_reg(request):
    return render(request, 'registration/succ_reg.html')
