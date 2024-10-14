from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.my_calendar, name='my_calendar'),
]
