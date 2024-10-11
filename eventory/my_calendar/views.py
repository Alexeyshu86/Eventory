from django.shortcuts import render

# Create your views here.
def my_calendar(request):
    return render(request, 'my_calendar.html')
