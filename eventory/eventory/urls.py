from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('', include('page_admin.urls'))
]
