from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from registration.models import CustomUser, Interest


def cabinet(request):
    user = CustomUser.objects.get(id=request.session.get('user_id'))
    context = {
        'user': user,
    }

    return render(request, 'cabinet/cabinet.html', context)


def change_data(request):
    user = CustomUser.objects.get(id=request.session.get('user_id'))
    interest_list = Interest.objects.all()
    context = {
        'user': user,
        'interest_list': interest_list,
    }
    # number = Person.objects.filter(id=1).update(name="Mike")

    if request.method == 'POST':
        first_name = request.POST.get('name')
        if first_name:
            first_name = CustomUser.objects.filter(id=user.id).update(first_name=first_name)

        last_name = request.POST.get('surname')
        if last_name:
            last_name = CustomUser.objects.filter(id=user.id).update(last_name=last_name)

        phone = request.POST.get('phone')
        if phone:
            phone = CustomUser.objects.filter(id=user.id).update(phone=phone)

        email = request.POST.get('email')
        if email:
            email = CustomUser.objects.filter(id=user.id).update(email=email)
            username = CustomUser.objects.filter(id=user.id).update(username=email)

        return HttpResponse(f'name: {first_name}\nlastname: {last_name}\nphone: {phone}\nemail: {email}')
    elif request.method == 'GET':
        return render(request, 'cabinet/change_data.html', context)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid change data'})


def logout_view(request):
    logout(request)
    return redirect('home')
