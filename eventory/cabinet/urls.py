from django.urls import path
from . import views

urlpatterns = [
    path('', views.cabinet, name='cabinet'),
    path('changedata/', views.change_data, name='change_data'),
]
