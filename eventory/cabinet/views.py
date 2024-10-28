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


def update_data(custom_user_model, interest_model, user_id):
    user = custom_user_model.objects.get(id=user_id)
    interest_list = interest_model.objects.all()

    context = {
        'user': user,
        'interest_list': interest_list,
    }
    return context


def update_password(old_password, new_password, user_id):
    user = CustomUser.objects.get(id=user_id)
    if check_password(old_password, user.password):
        user.set_password(new_password)
        user.save()
    else:
        return HttpResponse('Введите правильный пароль')


def change_data(request):

    user = CustomUser.objects.get(id=request.session.get('user_id'))
    context = update_data(CustomUser, Interest, user.id)

    if request.method == 'GET':
        return render(request, 'cabinet/change_data.html', context)

    elif request.method == 'POST':
        first_name = request.POST.get('name')
        if first_name:
            CustomUser.objects.filter(id=user.id).update(first_name=first_name)

        last_name = request.POST.get('surname')
        if last_name:
            CustomUser.objects.filter(id=user.id).update(last_name=last_name)

        phone = request.POST.get('phone')
        if phone:
            CustomUser.objects.filter(id=user.id).update(phone=phone)

        email = request.POST.get('email')
        if email:
            CustomUser.objects.filter(id=user.id).update(email=email)
            CustomUser.objects.filter(id=user.id).update(username=email)

        interests = request.POST.getlist('tags[]')
        if interests:
            CustomUser.objects.filter(id=user.id).update(interests=interests)

        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        if old_password and new_password:
            update_password(old_password, new_password, user.id)
        elif old_password and new_password == '':
            return HttpResponse('Введите новый пароль')
        elif old_password == '' and new_password:
            return HttpResponse('Введите старый пароль')

        return redirect('change_data')

    else:
        return JsonResponse({'success': False, 'error': 'Invalid change data'})


def logout_view(request):
    logout(request)
    return redirect('home')
