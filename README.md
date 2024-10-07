# Eventory
Это проект платформы для регистрации пользователей и организации событий, где каждый участник может подписываться на интересующие мероприятия. Проект предоставляет удобный личный кабинет для управления своим профилем, просмотра доступных событий, а также простой способ регистрации и участия в мероприятиях.

первый запуск Django

```commandline
django-admin startproject web
```

запуск локального сервера

```commandline
./manage.py runserver
```

активация виртуального окружения
```commandline
source ./venv/bin/activate 
```

деактивация
```commandline
deactivate
```

### Cоздание нового приложения

- создание приложения
```commandline
./manage.py startapp myapp
```

- Зарегистрировать приложение в настройках проекта:
В файле `settings.py` добавьте ваше приложение в список `INSTALLED_APPS`

```commandline
from django.urls import include, path

INSTALLED_APPS = [
    # Другие приложения
    'your_app_name',
]
```

- Настройка URL-ов (опционально):
  - Создайте файл `urls.py` в вашем приложении (если его еще нет).
  - В основном `urls.py` проекта добавьте `include()` для маршрутизации

```commandline
from django.urls import include, path

urlpatterns = [
    # Другие URL-ы
    path('your_app_name/', include('your_app_name.urls')),
]
```

- Миграции: Если в приложении используются модели, выполните миграции:
```commandline
python manage.py makemigrations your_app_name
python manage.py migrate
```
- Другие настройки (опционально):
  - Если необходимо, добавьте настройки для приложения в `settings.py`.
  - Зарегистрируйте модели в `admin.py`, если хотите управлять ими через административную панель: 
```commandline
from django.contrib import admin
from .models import YourModel

admin.site.register(YourModel)
```


