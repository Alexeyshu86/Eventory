from django.shortcuts import render

# Create your views here.
# def my_calendar(request):
#     context = {
#         'message': 'Это динамическое сообщение!'
#     }
#     return render(request, 'my_calendar/my_calendar.html', context)
def my_calendar(request):
    events = {
        'Январь': {
            'name': 'Новогодняя вечеринка',
            'interest': 'IT',
            'date': '1 января 2024',
            'time': '14:00',
            'organizer': 'ООО "Ромашка"',
            'subscribe': False
        },
        'Февраль': {
            'name': 'День святого Валентина',
            'interest': 'Team',
            'date': '14 февраля 2024',
            'time': '18:00',
            'organizer': 'Клуб \"Любовь\"',
            'subscribe': True
        },
        'Март': {
            'name': '8 Марта',
            'interest': 'Businuss',
            'date': '8 марта 2024',
            'time': '12:00',
            'organizer': 'Женская ассоциация',
            'subscribe': False
        },
        'Апрель': {
            'name': 'Пасха',
            'interest': 'Businuss',
            'date': '5 апреля 2024',
            'time': '10:00',
            'organizer': 'Приход \"Светлая Надежда\"',
            'subscribe': False
        },
        'Май': {
            'name': 'День Победы',
            'interest': 'Businuss',
            'date': '9 мая 2024',
            'time': '11:00',
            'organizer': 'Городская администрация',
            'subscribe': False
        },
        'Июнь': {
            'name': 'Летний фестиваль',
            'interest': 'IT',
            'date': '20 июня 2024',
            'time': '15:00',
            'organizer': 'Центр культуры',
            'subscribe': True
        },
        'Июль': {
            'name': 'День города',
            'interest': 'Businuss',
            'date': '12 июля 2024',
            'time': '17:00',
            'organizer': 'Городская администрация',
            'subscribe': False
        },
        'Август': {
            'name': 'День Независимости',
            'interest': 'Basketbol',
            'date': '24 августа 2024',
            'time': '16:00',
            'organizer': 'Государственный комитет',
            'subscribe': False
        },
        'Сентябрь': {
            'name': 'День знаний',
            'interest': 'Biatlon',
            'date': '1 сентября 2024',
            'time': '09:00',
            'organizer': 'Школьный совет',
            'subscribe': True
        },
        'Октябрь': {
            'name': 'Хэллоуин',
            'interest': 'Cars',
            'date': '31 октября 2024',
            'time': '19:00',
            'organizer': 'Клуб \"Магия\"',
            'subscribe': False
        },
        'Ноябрь': {
            'name': 'День благодарения',
            'interest': 'Moto',
            'date': '28 ноября 2024',
            'time': '18:30',
            'organizer': 'Семейный центр',
            'subscribe': False
        },
        'Декабрь': {
            'name': 'Рождество',
            'interest': 'Dakar',
            'date': '25 декабря 2024',
            'time': '15:00',
            'organizer': 'Церковь \"Радость\"',
            'subscribe': True
        }
    }

    return render(request, 'my_calendar/my_calendar.html', {'events': events})

def my_test_calendar(request):
    context = {
        'message': 'Это 2-я страница!'
    }
    return render(request, 'my_calendar/my_test_calendar.html', context)
