from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_registration, name='user_registration'),
    path('succ_reg/', views.succ_reg, name='succ_reg'),
    path('event_registration/', views.event_registration, name='event_registration'),
]