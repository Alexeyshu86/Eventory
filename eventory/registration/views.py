from django.shortcuts import render
from .models import CustomUser, Interest


def get_interests():
    return Interest.objects.all()

def user_registration(request):
    # user = CustomUser.objects.create_user(
    #     username = 'probe@m.ru',
    #     email = 'probe@m.ru',
    #     password = 'my_password',
    #     first_name = 'Alexey',
    #     last_name = 'Shushakov',
    #     phone = '89538794883'
    # )

    interest_list = get_interests()

    return render(request, 'registration/user_regs.html', {'interest_list': interest_list})
