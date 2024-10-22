from django.db import models
# from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from registration.models import Event, CustomUser

from .translate_month import gerate_dict_mounth_rus_name


class EventUser(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    subscribe = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user_id', 'event_id')  # Уникальная пара событие-пользователь

    def __str__(self):
        return f"{self.user_id.username} subscribed to {self.event_id.title}"

    # возвращает все события
    def get_all_event(self):
        return Event.objects.prefetch_related('eventuser_set')

    @classmethod
    def get_sub_eventuser(cls, user_id):
        user = get_object_or_404(CustomUser, id=user_id)

        return Event.objects.filter(eventuser__user_id=user, eventuser__subscribe=True)

def get_all_events_by_month():
    # Создаем словарь для хранения событий, сгруппированных по месяцам
    month_translation = gerate_dict_mounth_rus_name()

    events = Event.objects.prefetch_related('eventuser_set').all()
    # events = EventUser.get_sub_eventuser(1)

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
                'interest': event.interest,
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
