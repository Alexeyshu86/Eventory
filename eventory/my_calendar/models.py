import calendar

from django.db import models

# Create your models here.
class Event(models.Model):

    objects = None
    interest_id = models.IntegerField()
    user_id = models.IntegerField()
    name = models.CharField(max_length=30, blank=False)
    date = models.DateField()
    time = models.TimeField()
    organizer = models.CharField(max_length=30, blank=False)
    subscribe = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

def get_filtered_events():
    # Начальный запрос: выбираем все события
    events = Event.objects.all()

    # # Применяем фильтр по интересу, если он указан
    # if interest:
    #     events = events.filter(interest=interest)
    #
    # # Применяем фильтр по дате начала, если указано
    # if date_from:
    #     events = events.filter(date__gte=date_from)  # Дата >= date_from
    #
    # # Применяем фильтр по дате окончания, если указано
    # if date_to:
    #     events = events.filter(date__lte=date_to)  # Дата <= date_to

    return events

def get_all_events():
    # Получаем все события из базы данных
    events = Event.objects.all()

    # Преобразуем queryset в список словарей
    event_list = [
        {
            'name': event.name,
            # 'interest': event.interest,
            'date': event.date.strftime('%d %B %Y'),
            'time': event.time.strftime('%H:%M'),
            'organizer': event.organizer,
            # 'subscribe': event.subscribe
        }
        for event in events
    ]

    return event_list

def get_all_events_grouped_by_month():
    # Словарь для перевода названий месяцев на русский
    month_translation = {
        'January': 'январь', 'February': 'февраль', 'March': 'март',
        'April': 'апрель', 'May': 'май', 'June': 'июнь',
        'July': 'июль', 'August': 'август', 'September': 'сентябрь',
        'October': 'октябрь', 'November': 'ноябрь', 'December': 'декабрь'
    }

    # Создаем словарь для хранения событий, сгруппированных по месяцам
    events_by_month = {month: [] for month in month_translation.values()}

    # Получаем все события из базы данных
    events = Event.objects.all()

    # Создаем словарь для хранения событий, сгруппированных по месяцам
    # events_by_month = {month: [] for month in calendar.month_name[1:]}  # Создаем ключи для каждого месяца

    for event in events:
        # Получаем название месяца на английском и переводим на русский
        month_name_english = event.date.strftime('%B')
        month_name_russian = month_translation.get(month_name_english, '').lower()

        # Добавляем событие в соответствующий месяц
        if month_name_russian in events_by_month:
            events_by_month[month_name_russian].append({
                'name': event.name,
                # 'interest': event.interest,
                'date': event.date.strftime('%d %B %Y'),
                'time': event.time.strftime('%H:%M'),
                'organizer': event.organizer,
                # 'subscribe': event.subscribe
            })

    return events_by_month