# Задание 1 Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


# Num = input('Введите число: ')
# sum_ = 0
# for i in Num:
#     if i.isdigit():
#         sum_ += int(i)
# print(int(sum_))


# Задание 2 Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:   пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# def create_list(n):
#     temp = []
#     mult_n = 1
#     for i in range(1, n + 1):
#         mult_n *= i
#         temp.append(mult_n)
#     return temp
#
#
# numb = create_list(int(input('Enter n: ')))
# print(numb)


# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
# Пример:   Для n = 6 -> 14.072


# N = int(input('Enter number: '))
# list = []
# sum = 0
# for i in range(1, N + 1):
#     Ni = round((1 + (1 / i)) ** i, 3)
#     list.append(Ni)
#     sum += round(Ni, 3)
# print(list)
# print(f'N = {N} -> {sum}')


# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.


# def create_list(n):
#     temp = []
#     for i in range(-n, n + 1):
#         temp.append(i)
#     return temp
#
#
# numb = create_list(int(input('Enter n: ')))
# num_1 = int(input('Enter num_1: '))
# num_2 = int(input('Enter num_2: '))
# mult_pos = numb[num_1] * numb[num_2]
# print(numb)
# print(f'{numb[num_1]} * {numb[num_2]} = {mult_pos}')


# Задание 5 Реализуйте алгоритм перемешивания списка.
# можно использовать  random.randint(2, 6)
#                     random.randrange(2, 6)


# import random
#
#
# temp = []
# n = int(input('Enter n: '))
# min_ = int(input('Enter min: '))
# max_ = int(input('Enter max: '))
#
#
# for i in range(n):
#     temp.append(random.randint(min_, max_))
# print('The original list -> ' + str(temp))
#
#
# for i in range(len(temp) - 1, 0, -1):
#     j = random.randint(0, i+1)
#     temp[i], temp[j] = temp[j], temp[i]
# print('The shuffled list -> ' + str(temp))
