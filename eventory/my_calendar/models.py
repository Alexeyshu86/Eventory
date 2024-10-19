from django.db import models
from django.contrib.auth.models import User

from eventory.registration.models import Event

# from registration.models import Event

# Interest
# class Interest(models.Model):
#     interest = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.interest
#
# # Create your models here.
# class Event(models.Model):
#
#     interest_id = models.ForeignKey(Interest, on_delete=models.CASCADE, db_column='interest_id')
#     title = models.CharField(max_length=30, blank=False)
#     date = models.DateField()
#     time = models.TimeField()
#     organizer = models.CharField(max_length=30, blank=False)
#
#     def __str__(self):
#         return f"{self.title}"

class EventUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    subscribe = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user_id', 'event_id')  # Уникальная пара событие-пользователь

    def __str__(self):
        return f"{self.user_id.username} subscribed to {self.event_id.title}"

def get_all_events_grouped_by_month():
    # Словарь для перевода названий месяцев на русский
    month_translation = {
        'January': 'январь', 'February': 'февраль', 'March': 'март',
        'April': 'апрель', 'May': 'май', 'June': 'июнь',
        'July': 'июль', 'August': 'август', 'September': 'сентябрь',
        'October': 'октябрь', 'November': 'ноябрь', 'December': 'декабрь'
    }

    # events_users = EventUser.objects.select_related('event_id').all()
    events = Event.objects.prefetch_related('eventuser_set').all()

    # Создаем словарь для хранения событий, сгруппированных по месяцам
    events_by_month = {month: [] for month in month_translation.values()}

    for event in events:
        # Получаем название месяца на английском и переводим на русский
        month_name_english = event.date.strftime('%B')
        month_name_russian = month_translation.get(month_name_english, '').lower()

        for event_user in event.eventuser_set.all():
            if month_name_russian in events_by_month:
                events_by_month[month_name_russian].append({
                    'event_id': event.id,
                    'title': event.title,
                    'interest': event.interest_id,
                    'date': event.date.strftime('%d %B %Y'),
                    'time': event.time.strftime('%H:%M'),
                    'organizer': event.organizer,
                    'subscribe': event_user.subscribe  # Получаем значение subscribe
                })

    return events_by_month

def get_all_events_by_month():
    # Словарь для перевода названий месяцев на русский
    month_translation = {
        'January': 'январь', 'February': 'февраль', 'March': 'март',
        'April': 'апрель', 'May': 'май', 'June': 'июнь',
        'July': 'июль', 'August': 'август', 'September': 'сентябрь',
        'October': 'октябрь', 'November': 'ноябрь', 'December': 'декабрь'
    }

    events = Event.objects.prefetch_related('eventuser_set').all()

    # Создаем словарь для хранения событий, сгруппированных по месяцам
    events_by_month = {month: [] for month in month_translation.values()}

    for event in events:
        # Получаем название месяца на английском и переводим на русский
        month_name_english = event.date.strftime('%B')
        month_name_russian = month_translation.get(month_name_english, '').lower()

        # Добавляем событие в словарь, даже если нет связанных записей EventUser
        if month_name_russian in events_by_month:
            event_data = {
                'event_id': event.id,
                'title': event.title,
                'interest': event.interest_id,
                'date': event.date.strftime('%d %B %Y'),
                'time': event.time.strftime('%H:%M'),
                'organizer': event.organizer,
                'subscribe': None  # Указываем None, если нет данных о подписке
            }
            if event.eventuser_set.exists():
                for event_user in event.eventuser_set.all():
                    # Если есть связанные записи EventUser, обновляем значение подписки
                    event_data['subscribe'] = event_user.subscribe
            events_by_month[month_name_russian].append(event_data)


    return events_by_month
