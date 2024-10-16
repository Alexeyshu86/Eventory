from django.shortcuts import render, HttpResponse, redirect
from .models import CustomUser, Interest


def user_registration(request):

    error_passw_repeat = None
    interest_list = Interest.objects.all()

    if request.method == 'POST':
        t_surname = request.POST.get('surname')
        t_name = request.POST.get('name')
        t_phone = request.POST.get('phone')
        t_email = request.POST.get('email')
        t_list_interest = request.POST.getlist('tags[]')
        t_password = request.POST.get('password')
        t_password_repeat = request.POST.get('password_repeat')
        if t_password_repeat != t_password:
            error_passw_repeat = 'Пароли не совпадают.'
            return render(request, 'registration/user_regs.html',
                          {'interest_list': interest_list, 'error_passw_repeat': error_passw_repeat})
        try:
            user = CustomUser.objects.create_user(
                username=t_email,
                email=t_email,
                password=t_password,
                first_name=t_name,
                last_name=t_surname,
                phone=t_phone
            )
            return redirect('home')
        except Exception as e:
            return HttpResponse(f'Ошибка при создании пользователя: {str(e)}')
    else:
        return render(request, 'registration/user_regs.html',
                      {'interest_list': interest_list, 'error_passw_repeat': error_passw_repeat})
