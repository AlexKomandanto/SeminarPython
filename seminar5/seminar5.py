# a = [(1, 2), (3, 3), (-2, 1), (6, 5), (6, -5)]
#
# print(max(a, key=lambda x: x[1])) # срвнение по одному элементу c lambda

# a = ['1', '2', '10', '9']
#
# print(max(a, key=int))   # срвнение как числа


# List Comprehension
# a = []
# for n in range(11):     # от куда добавляем
#     a.append(n * n)     # что берется для list
#
# print(a)

# b = [n * n for n in range(11)]  # сразу пишем значения append, дальше от куда добавляем
# print(b)

#
# b = [n / 10 for n in range(0, 31, 2)]  # вывод дробных значений
# print(b)
#
# from random import random, randint, randrange
#
# print(50 + random() * 50)
# print(randint(50, 100))
# print(randrange(50, 101))
#
# a = []
# for n in range(11):         # от куда добавляем
#     if n % 5 != 0:
#         if n % 2 == 0:
#             a.append(n * n)     # что берется для list
#         else:
#             a.append(n**3)      # возведение в куб
#
#
#
# print(a)
# #  как записать в List Comprehension
# # [exp for item in iterable]
# # [exp for item in iterable (if conditional)]
# # [exp <if conditional> for item in iterable (if conditional)]
#
# b = [n * n if n % 2 == 0 else n**3 for n in range(11) if n % 5 != 0]
#
# print(b)
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# itog = tuple(map(lambda x: x ** 2, a))
#
# filter_itog = list(filter(lambda x: x % 5!= 0, a))
#
# print(filter_itog)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# b = 'abcdefghi'
#
# c = (False, True, None)
#
# for item in zip(a,b,c): # применение zip
#     print(item)


# 1 2 3 4 6 7 8 9
#
# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.
#
# with open("file_task1", "w", encoding="UTF-8") as data_file:
#     data_file.write("1 2 3 4 5 7 8 9")                      # создали файл и записали в него данные
# with open("file_task1", "r", encoding="UTF-8") as data_file:
#     string = data_file.readline()                            # открыли файл и прочитали с него данные
# string = list(map(int, string.split()))             # сохранили в переменную данные и перевели их численные инт
# a = 0
# for i in range(1, len(string)):
#     if string[i] - 1 != string[i - 1]:               # прошли 1й список по элемента и сравнили со 2м
#         a = i
#
# print(string[a]-1)           # вывели полученное значение

# with open("file_task1", "w", encoding="UTF-8") as data_file:
#     data_file.write("1 2 3 4 5 7 8 9")                      # создали файл и записали в него данные
# with open("file_task1", "r", encoding="UTF-8") as data_file:
#     string = data_file.readline()                            # открыли файл и прочитали с него данные
# string = list(map(int, string.split()))
#
# for i1, i2 in zip(string, range(string[0], string[0] + len(string))):
#     if i1 != i2:
#         print(i2)
#         break


# 2. Напишите программу, удаляющую из текста все слова, содержащие "абв". <- filter

# with open("file_task2", "w", encoding="UTF-8") as data_file:
#     data_file.write("дым кротав привет эд фабав рабв ")                      # создали файл и записали в него данные
# with open("file_task2", "r", encoding="UTF-8") as data_file:
#     string = data_file.readline().split()
# # string = list(map(str, string.split()))
# # a = "абв".split()
# # a = map("абв")
# # filter_itog = list(filter(lambda x: "абв" not in x, string))
# #
# # print(filter_itog)
# list_ = list(map(str, string))
# def true_or_not(string):
#     return "абв" in string
# result_filter = filter(true_or_not, list_)
# for i in result_filter:
#     print(i)
