# cook_book = [
#     ['Салат',
#       [
#         ['картофель', 100, 'гр.'],
#         ['морковь', 50, 'гр.'],
#         ['огурцы', 50, 'гр.'],
#         ['горошек', 30, 'гр.'],
#         ['маойнез', 70, 'мл.'],
#       ]
#     ],
#     ['Пицца',
#       [
#           ['сыр', 50, 'гр.'],
#           ['томаты', 50, 'гр.'],
#           ['тесто', 100, 'гр.'],
#           ['бекон', 30, 'гр.'],
#           ['колбаса', 30, 'гр.'],
#           ['грибы', 20, 'гр.'],
#       ],
#     ],
#     ['Фруктовый десерт',
#        [
#           ['хурма', 60, 'гр.'],
#           ['киви', 60, 'гр.'],
#           ['творог', 60, 'гр.'],
#           ['сахар', 10, 'гр.'],
#           ['мед', 50, 'мл.'],
#        ]
#     ]
#  ]
# person=int(input('Введите количество персон:'))
#
# for name, ingridients in cook_book:
#   print()
#   print (name+':')
#   for ingridient in ingridients:
#       sost_name=ingridient[0]
#       kolichestvo=(ingridient[1])*person
#       print(f"{sost_name}, {kolichestvo}{ingridient[2]}")


def print_person(name, age = 18):
    print(f"Name: {name}  Age: {age}")


print_person("Bob")
print_person("Tom", 37)