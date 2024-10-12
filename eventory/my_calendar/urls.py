from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.my_calendar, name='my_calendar'),
    path('test_calendar/', views.my_test_calendar, name='my_test_calendar')
]
