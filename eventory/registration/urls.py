from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_registration, name='user_registration'),
    path('succreg/', views.succ_reg, name='succ_reg'),
    path('event_registration/', views.event_registration, name='event_registration'),
    path('succeventreg/', views.succ_event_reg, name='succ_event_reg'),
]