# name = "Коля"
# age = 13
# print(f'Меня зовут {name}. Я родился в {2022 - age} году.')
# pole = 'Hello Word'
# print(pole[2])
# print(pole[-4])
# print(pole[0:5])
# print(pole[0:8:2])
# print(pole[6:])
# print(pole[:5])

# num = int(123456)
# num_3 = int (num[2])
# print(num_3)

# Работа со списками
month_list = ["Jan", 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
income_list = [13000, 14000, 14300, 15000, 13800, 13000, 14900, 15200, 15300]
income_by_month = [['Jan', 13000], ['Feb', 14000], ['Mar', 14300], ['Apr', 15000], ['May', 13800], ['Jun', 13000], ['Jul', 14900], ['Aug', 15200], ['Sep', 15300]]
# print(income_list.count(14000))
# #
# print(month_list[0])
# print(month_list[-1])
# print(income_by_month[-4][0][0])
# income_by_month[1][1] = 120000
# print(income_by_month)
# income_by_month_2 = [['Nov', 15400], ["Dec", 17000]]
# income_by_month = income_by_month + income_by_month_2
# print(income_by_month)
# del (income_by_month[-1])
# print(income_by_month)

# month_list.remove('Jan')
# month_list.remove('Jun')
# print(month_list)
# income_by_month.append(['Dec', 17000])
# print(income_by_month)
# income_by_month.insert(2, ['Noember', 11200])
# print(income_by_month)
# print(income_list.index(14000))
# month_list.reverse()
# print(month_list)
# print(sorted(income_list))
# print(income_list)
# print(income_list.sort())
# print(income_list)
# string = "смотреть сериалы онлайн, новости спорта, афиша кино, курс доллара, сериалы этим летом, курс по питону, сериалы про спорт"
# print(sorted(income_by_month))
# print(string.split(','))
# print('\n'.join(['Столбец 1', 'Столбец 2','Столбец 3']))
# salary_tuple = (1000, 1200, 1300, 900, 800)
# my_list = (list(salary_tuple))
# print(type(salary_tuple))
#
# salaries = [1000, 1200, 1300, 900, 800, 1000]
# names = ['Robert', 'Jane', 'Liza', ' Richard', 'John']
# salaries_by_names = (zip(names,salaries))
# print(salaries_by_names)
# print(list(salaries_by_names))
# print(type(salaries_by_names))
# company_tuple = ('Orange', 1000000, 20000)
# company_name, capitalization, people = company_tuple
# print('company_name \t- ', company_name)
# print('capitalization \t- ', capitalization)
# print('people \t\t\t- ', people)
# print('Hello1' in "Hello Word")
# print('Jan' not in month_list)
# x = 5
# while x != 0 :
#     x -=1
#     print (x)
#
# x = 7
# while x != 0:
#     if x % 2 == 0:
#         print(x, '- Чётное число')
#     else:
#         print(x, '- Нечётное число')
#      x -= 1
# sum = 0
# x ='100'
# while x != 0:
#     x = int(input('Введите число: '))
#     sum += x
#
# print('Сумма всех чисел = ', sum)
# company_name = 'Orange'
# for letter in company_name:
#     letter = letter.upper()
#     print(letter, end='')
# comp_cap= [['Orange', 1.3], ['Maxisoft', 1.5], ['Headbook', 0.8], ['Nicola', 2.2]]
# for comp in comp_cap:
#     # print(comp)
#     print(f"{comp[0]} \tКапитализация компании {comp[1]}")
#
# comp_cap= [['Orange', 1.3], ['Maxisoft', 1.5], ['Headbook', 0.8], ['Nicola', 2.2]]
# for comp, cap in comp_cap:
#     # print(comp)
#     print(f"{comp} \tКапитализация компании {cap}")
# phrase = '640Кб должно хватать для любых задач. Билл Гейтс (По легенде)'

# for letter in phrase:
#     if letter == ' ':
#         pass
#     print(letter, end='')
# professions = ['IT', 'Физика', 'Математика']
# persons = [['Гейтс', 'Джобс', 'Возняк'], ['Энштейн', 'Фейнман'], ['Эвклин', 'Ньютон']]
#
# for prof, names in zip(professions, persons):
#     # print()
#     print(f'{prof:}')
#     for name in names:
#         print(name)
#     print()
#
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# boys_sort=sorted(boys)
# girls_sort=sorted(girls)
# x=len(boys)
# y=len(girls)
# if x != y:
#     print('Внимание!!! Кто-то может остаться без пары:')
# else:
#     print('Идеальные пары:')
#     for name in zip (boys_sort, girls_sort):
#         print(f"{name[0]} и {name[1]}")
#
cook_book = [
    ['Салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['маойнез', 70, 'гр.'],
      ]
    ],
    ['Пицца',
      [
          ['сыр', 50, 'гр.'],
          ['томаты', 50, 'гр.'],
          ['тесто', 100, 'гр.'],
          ['бекон', 30, 'гр.'],
          ['колбаса', 30, 'гр.'],
          ['грибы', 20, 'гр.'],
      ],
    ],
    ['Фруктовый десерт',
       [
          ['хурма', 60, 'гр.'],
          ['киви', 60, 'гр.'],
          ['творог', 60, 'гр.'],
          ['сахар', 10, 'гр.'],
          ['мед', 50, 'мл.'],
       ]
    ]
 ]
person = 5
# name = cook_book[0][0]
# print(name)
for dish, ingrediets in cook_book:
   print(dish)
   for ingredient in ingrediets:
       ingredient_name = ingredient[0]
       ingredient_ves = ingredient[1]
       ingredient_massa= ingredient[2]
       print(f"{ingredient_name}, {ingredient_ves}{ingredient_massa}")
   print()
   # salat= (f"{ingridient}, {ves*person}{massa}")
   # print(salat)

# name = cook_book[1][0]
# print()
# print(name)
# for ingridient, ves, massa in (cook_book[1][1]):
#     pizza= (f"{ingridient}, {ves*person}{massa}")
#     print(pizza)
#
# name = cook_book[2][0]
# print()
# print(name)
# for ingridient, ves, massa in (cook_book[2][1]):
#     frukt= (f"{ingridient}, {ves*person}{massa}")
#     print(frukt)


# # Вариант, когда исходные блюда вводят отдельно
#
# salat_1 = int(input('Введите количество салатов: '))
# pizza_1 = int(input('Введите количество пицци:'))
# frukt_1 = int(input('Введите количество дерерта:'))
# print("\n" * 100)
# name = cook_book[0][0]
# print(name)
# for ingridient, ves, massa in (cook_book[0][1]):
#     salat= (f"{ingridient}, {ves*salat_1}{massa}")
#     print(salat)
#
# name = cook_book[1][0]
# print()
# print(name)
# for ingridient, ves, massa in (cook_book[1][1]):
#     pizza= (f"{ingridient}, {ves*pizza_1}{massa}")
#     print(pizza)
#
# name = cook_book[2][0]
# print()
# print(name)
# for ingridient, ves, massa in (cook_book[2][1]):
#     salat= (f"{ingridient}, {ves*frukt_1}{massa}")
#     print(salat)
# person = int(input('Введите число'))



bvcxcbvxcv














