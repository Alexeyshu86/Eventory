from django.urls import path
from . import views
from .views import my_calendar

urlpatterns = [
    path('calendar/', views.my_calendar, name='my_calendar'),
]
