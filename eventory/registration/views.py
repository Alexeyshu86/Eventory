from django.shortcuts import render
from .models import CustomUser


def user_registration(request):
    # user = CustomUser.objects.create_user(
    #     username = 'probe@m.ru',
    #     email = 'probe@m.ru',
    #     password = 'my_password',
    #     first_name = 'Alexey',
    #     last_name = 'Shushakov',
    #     phone = '89538794883'
    # )
    return render(request, 'registration/user_regs.html')
