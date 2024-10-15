from django.shortcuts import render, HttpResponse
from .models import CustomUser, Interest
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


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

    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        list_interest = request.POST.getlist('tags[]')
        return HttpResponse(f'name: {name}\nsurname: {surname}\n'
                            f'phone: {phone}\nemail: {email}\n'
                            f'interests: {list_interest}')
    else:
        return render(request, 'registration/user_regs.html', {'interest_list': interest_list})
