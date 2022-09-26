# a = 'www'
# print(type(a))
# a = 51      # None - ничего
# print(type(a))
# and or not /  и или нет

# 1. Напишите программу, которая принимает на вход два числа и
#   проверяет, является ли одно число квадратом другого.
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8, 9 -> нет
# a = int(input('Введите a: \n'))  # \n печать на новой строке
# print('Введите b: ')
# b = int(input('b = '))
# if b == a * a:
#     print(f' {a}, {b} -> yes')
# elif a == b * b:
#     print(f' {a}, {b} -> yes')
# else:
#     print(f' {a}, {b} -> no')

# второй вариант решения с возведением в степень
# a = int(input('Введите a: \n'))
# b = int(input('Введите b: \n'))
#
# if b ** 2 == a or a ** 2 == b:
#     print('True!')
# else:
#     print('False!')

# 2. Напишите программу, которая на вход принимает 5 чисел
#   и находит максимальное из них.
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90
#
# def large(lst):
#     max_ = lst[0]
#     for i in lst:
#         if i > max_:
#             max_ = i
#     return max_
#
#
# lst = []
# for i in range(5):
#     lst.append(int(input(f'Введите {i + 1} число: ')))
# print(f'Максимальное число: {large(lst)} ')


# Задача: напишите программу,
# которая будет показывать целочисленные делители, введеного числа

# a = int(input('Введите число: '))
# result = []
# temp_a = a
#
# for i in range(2, a):
#     while temp_a % i == 0:
#         result.append(i)
#         temp_a = temp_a // i
#
# print(result, end=' ')   # end=' ' вывод в одну строку




