from django.shortcuts import render
from .models import Event, get_filtered_events, get_all_events, get_all_events_grouped_by_month

# Create your views here.
# def my_calendar(request):
#     events = {
#         'Январь': [
#             {
#                 'name': 'Новогодняя вечеринка',
#                 'interest': 'IT',
#                 'date': '1 января 2024',
#                 'time': '14:00',
#                 'organizer': 'ООО "Ромашка"',
#                 'subscribe': False
#             },
#             {
#                 'name': 'Зимний фестиваль',
#                 'interest': 'Спорт',
#                 'date': '15 января 2024',
#                 'time': '11:00',
#                 'organizer': 'Спортивный клуб',
#                 'subscribe': True
#             }
#         ],
#         'Февраль': [
#             {
#                 'name': 'День святого Валентина',
#                 'interest': 'Team',
#                 'date': '14 февраля 2024',
#                 'time': '18:00',
#                 'organizer': 'Клуб "Любовь"',
#                 'subscribe': True
#             },
#             {
#                 'name': 'Февральский концерт',
#                 'interest': 'Музыка',
#                 'date': '25 февраля 2024',
#                 'time': '19:00',
#                 'organizer': 'Концертный зал',
#                 'subscribe': False
#             }
#         ],
#         'Март': [
#             {
#                 'name': '8 Марта',
#                 'interest': 'Business',
#                 'date': '8 марта 2024',
#                 'time': '12:00',
#                 'organizer': 'Женская ассоциация',
#                 'subscribe': False
#             },
#             {
#                 'name': 'Весенняя ярмарка',
#                 'interest': 'Культура',
#                 'date': '21 марта 2024',
#                 'time': '10:00',
#                 'organizer': 'Городской центр',
#                 'subscribe': True
#             }
#         ],
#         'Апрель': [
#             {
#                 'name': 'Пасха',
#                 'interest': 'Религия',
#                 'date': '5 апреля 2024',
#                 'time': '10:00',
#                 'organizer': 'Приход "Светлая Надежда"',
#                 'subscribe': False
#             },
#             {
#                 'name': 'Апрельский турнир по шахматам',
#                 'interest': 'Спорт',
#                 'date': '18 апреля 2024',
#                 'time': '14:00',
#                 'organizer': 'Шахматный клуб',
#                 'subscribe': True
#             }
#         ],
#         'Май': [
#             {
#                 'name': 'День Победы',
#                 'interest': 'История',
#                 'date': '9 мая 2024',
#                 'time': '11:00',
#                 'organizer': 'Городская администрация',
#                 'subscribe': False
#             },
#             {
#                 'name': 'Весенний марафон',
#                 'interest': 'Спорт',
#                 'date': '20 мая 2024',
#                 'time': '08:00',
#                 'organizer': 'Беговой клуб',
#                 'subscribe': True
#             }
#         ],
#         'Июнь': [
#             {
#                 'name': 'Летний фестиваль',
#                 'interest': 'IT',
#                 'date': '20 июня 2024',
#                 'time': '15:00',
#                 'organizer': 'Центр культуры',
#                 'subscribe': True
#             },
#             {
#                 'name': 'Летний пикник',
#                 'interest': 'Отдых',
#                 'date': '22 июня 2024',
#                 'time': '16:00',
#                 'organizer': 'Центр отдыха',
#                 'subscribe': False
#             }
#         ],
#         'Июль': [
#             {
#                 'name': 'День города',
#                 'interest': 'Культура',
#                 'date': '12 июля 2024',
#                 'time': '17:00',
#                 'organizer': 'Городская администрация',
#                 'subscribe': True
#             },
#
#         ],
#         'Август': [
#             {
#                 'name': 'День Независимости',
#                 'interest': 'Политика',
#                 'date': '24 августа 2024',
#                 'time': '16:00',
#                 'organizer': 'Государственный комитет',
#                 'subscribe': False
#             },
#             {
#                 'name': 'Августовская вечеринка на пляже',
#                 'interest': 'Отдых',
#                 'date': '28 августа 2024',
#                 'time': '18:00',
#                 'organizer': 'Пляжный клуб',
#                 'subscribe': True
#             },
#             {
#                 'name': 'Августовская  пляже',
#                 'interest': 'О',
#                 'date': '29 августа 2024',
#                 'time': '19:00',
#                 'organizer': 'Пляжный клуб',
#                 'subscribe': True
#             }
#         ],
#         'Сентябрь': [
#             {
#                 'name': 'День знаний',
#                 'interest': 'Образование',
#                 'date': '1 сентября 2024',
#                 'time': '09:00',
#                 'organizer': 'Школьный совет',
#                 'subscribe': True
#             },
#             {
#                 'name': 'Осенний музыкальный фестиваль',
#                 'interest': 'Музыка',
#                 'date': '19 сентября 2024',
#                 'time': '18:00',
#                 'organizer': 'Музыкальный центр',
#                 'subscribe': False
#             }
#         ],
#         'Октябрь': [
#             {
#                 'name': 'Хэллоуин',
#                 'interest': 'Культура',
#                 'date': '31 октября 2024',
#                 'time': '19:00',
#                 'organizer': 'Клуб "Магия"',
#                 'subscribe': False
#             },
#             {
#                 'name': 'Осенний турнир по футболу',
#                 'interest': 'Спорт',
#                 'date': '15 октября 2024',
#                 'time': '17:00',
#                 'organizer': 'Футбольная ассоциация',
#                 'subscribe': True
#             }
#         ],
#         'Ноябрь': [
#             {
#                 'name': 'День благодарения',
#                 'interest': 'Культура',
#                 'date': '28 ноября 2024',
#                 'time': '18:30',
#                 'organizer': 'Семейный центр',
#                 'subscribe': False
#             },
#             {
#                 'name': 'Осенняя выставка искусств',
#                 'interest': 'Искусство',
#                 'date': '5 ноября 2024',
#                 'time': '14:00',
#                 'organizer': 'Галерея "Современное искусство"',
#                 'subscribe': True
#             }
#         ],
#         'Декабрь': [
#             {
#                 'name': 'Рождество',
#                 'interest': 'Религия',
#                 'date': '25 декабря 2024',
#                 'time': '15:00',
#                 'organizer': 'Церковь "Радость"',
#                 'subscribe': True
#             },
#             {
#                 'name': 'Новогодняя ярмарка',
#                 'interest': 'Культура',
#                 'date': '30 декабря 2024',
#                 'time': '12:00',
#                 'organizer': 'Центр города',
#                 'subscribe': False
#             }
#         ]
#     }
#     print("set = ", events)
#
#     return render(request, 'my_calendar/my_calendar.html', {'events': events})

# def my_calendar(request):
#     # Получаем параметры фильтра из запроса (например, ?interest=IT&date_from=2024-01-01)
#
#     # interest = request.GET.get('interest')
#     # date_from = request.GET.get('date_from')
#     # date_to = request.GET.get('date_to')
#
#     # Вызываем функцию фильтрации
#     # events = get_filtered_events()
#     # events = get_filtered_events()
#     # events = get_filtered_events()
#     events = get_all_events_grouped_by_month()
#     events_1 = get_all_events()
#     print("словарь событий:", events)
#
#     # Отправляем отфильтрованные события в шаблон
#     return render(request, 'my_calendar/my_calendar.html', {'events': events})

def my_calendar(request):


    events = get_all_events_grouped_by_month()
    print("словарь событий:", events)

    # Отправляем отфильтрованные события в шаблон
    return render(request, 'my_calendar/my_calendar.html', {'events': events})

