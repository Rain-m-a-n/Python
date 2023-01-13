# capital_dict = {'Russia': 'Moscow', 'Ukraine': 'Kiev'}
# capital_dict['France'] = 'Paris'
# for country, city in capital_dict.items():
#   print(f"{country} -> {city}")

courses_list= [
  {"title": "Java-разработчик с нуля",
   "mentors": ["Павел Дерендяев","Алексей Яковлев", "Сергей Сердюк"], "duration":11},
  {"title": "Веб-разработчик с нуля",
   "mentors": ["Николай Лопин", "Алена Батицкая", "Алексей Дацков", "Александр Беспоясов"], "duration":19},
  {"title": "Frontend - разработчик с нуля",
   "mentors": ["Ильназ Гиязов", "Татьяна Тен", "Алена Батицкая", "Александр Фитискин", "Владимир Чебукин", "Эдгар Нуррулин"], "duration":13}
]
# for course in courses_list:
#     print("Название курса: {}".format(course['title']))
#     print("Преподователи курса: {}".format(",".join(course["mentors"])))
#     print()
#
# max_count = 0
# leader_id = -1
# for id, course in enumerate(courses_list):
#     print("Название курса: {}".format(course['title']))
#   count = len(course["mentors"])
#   print(f"Количество преподавателей: {count}")
#   if count > max_count:
#     max_count = count
#     leader_id = id
# print("Наш лидер - курс {}, преподователей: {}".format(courses_list[id]["title"], len(courses_list[id]["mentors"])))
#
new_dict={}
new_dict.setdefault("title", "C++")
new_dict.setdefault("mentors", ["Елена Петровна"])
# new_dict["mentors"].append("Олег Булыгин")
# new_dict.setdefault("durations", 15)
# print(new_dict)
# print(new_dict.keys())


java_set = set(courses_list[0]["mentors"])
web_set = set(courses_list[1]["mentors"])
frontend_set = set(courses_list[2]["mentors"])
print(java_set)
# print(f"{type(java_set)}, {java_set}")
#
# print(f"java & web: {java_set & web_set}")
# print(f"java & frontend: {java_set & frontend_set}")
# print(f"web & frontend: {web_set & frontend_set}")

# print(f" Разность Frontend and web: {frontend_set - web_set}")
#
# print("наоборот")
# print(f" Разность Frontend and web: {web_set - frontend_set}")
#
# print(f"симметрическая разность front -web: {frontend_set ^ web_set}")
# print(f"симметрическая разность web - front: {web_set.symmetric_difference(frontend_set)}")

