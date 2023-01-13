# geo_logs = [
#     {'visit1': ['Москва', 'Россия']},
#     {'visit2': ['Дели', 'Индия']},
#     {'visit3': ['Владимир', 'Россия']},
#     {'visit4': ['Лиссабон', 'Португалия']},
#     {'visit5': ['Париж', 'Франция']},
#     {'visit6': ['Лиссабон', 'Португалия']},
#     {'visit7': ['Тула', 'Россия']},
#     {'visit8': ['Тула', 'Россия']},
#     {'visit9': ['Курск', 'Россия']},
#     {'visit10': ['Архангельск', 'Россия']}
# ]
# for visit in geo_logs:
#     value = list(visit.values())[0][1]
#     if value == 'Россия':
#       print(visit)

# ids = {'user1': [213, 213, 213, 15, 213],
#        'user2': [54, 54, 119, 119, 119],
#        'user3': [213, 98, 98, 35]}
# value= set()
# for geo_ids in ids.values():
#     value |= set(geo_ids)
# print(list(value))


queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
#     ]
# typ2=0
# typ3=0
# typ_all=0
# for long in queries:
#     slov=len(long.split())
#     if slov == 2:
#        typ2 = typ2 + 1
#        typ_all = typ_all + 1
#     else:
#        typ3 = typ3 + 1
#        typ_all = typ_all + 1
# poisk2 = (typ2 * 100) // typ_all
# poisk3 = (typ3 * 100) // typ_all
# print(f" Поисковых запросов из двух слов: {poisk2}%\n Поисковых запросов из трех слов: {poisk3}%")

