# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint
#
# n = int(input('Укажите размер списка: '))
# min_ = int(input('Введите минимальное значение диапазона: '))
# max_ = int(input('Введите максимальное значение диапазона: '))
# summ_nums = 0
# my_list = []
#
# for i in range(n):
#     my_list.append(randint(min_, max_))
# print(my_list)
#
# for index in range(len(my_list)):
#     if index % 2 == 1:
#         summ_nums += my_list[index]
# print(summ_nums)

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# r = int(input('Введите длину массива: '))
# my_list = []
# print('Введите элементы массива, таким колличеством элеменнтов -> ', r)
# for i in range(r):
#     num = int(input())
#     my_list.append(num)
# print(my_list)
#
# list_result = []
#
# for i in range((len(my_list) + 1) // 2):
#     list_result.append(my_list[i] * my_list[len(my_list) - 1 - i])
# print(list_result)

# 2 решение через random
# import random
#
# n = int(input('Укажите размер списка: '))
# min_ = int(input('Введите минимальное значение диапазона: '))
# max_ = int(input('Введите максимальное значение диапазона: '))
# my_list = []
#
# for i in range(n):
#     my_list.append(random.randint(min_, max_))
# print(my_list)
#
# result_list = []
#
# for i in range((len(my_list) + 1) // 2):
#     result_list.append(my_list[i] * my_list[len(my_list) - 1 - i])
# print(result_list)

# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random
#
# n = int(input('Укажите размер списка: '))
# min_ = int(input('Введите минимальное значение диапазона: '))
# max_ = int(input('Введите максимальное значение диапазона: '))
# my_list = []
#
# for i in range(n):
#     my_list.append(random.uniform(min_, max_))
#     my_list = [round(i, 3) for i in my_list]
# print(my_list)
#
# max_fract = my_list[0] % 1
# min_fract = my_list[0] % 1
# for i in range(1, len(my_list)):
#     if my_list[i] % 1 > max_fract:
#         max_fract = my_list[i] % 1
#     if my_list[i] % 1 < min_fract:
#         min_fract = my_list[i] % 1
# print(f'Максимальное значение дробной части: {round(max_fract, 3)}')
# print(f'Минимальное значение дробной части: {round(min_fract, 3)}')
# print(f'Разность между максимальным и минимальным значением дробной части: {round(max_fract - min_fract, 3)}')


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Первый способ

# num = int(input('Укажите число в десятичной системе счисления: '))
# print(f'{num:b}')


# Второй способ

# num = int(input('Укажите число в десятичной системе счисления: '))
# num_bin = ''
#
# while num > 0:
#     num_bin = str(num % 2) + num_bin
#     num = num // 2
#
# print(num_bin)

# 5. Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# def Fibonacci(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
#
# def NegaFibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2
#
# my_list = [0]
# k = int(input('Введите число: '))
# for i in range(1, k + 1):
#     my_list.append(Fibonacci(i))
#     my_list.insert(0, NegaFibonacci(i))
# print(my_list)


# n = 10
# fib = [0, 1]
#
# for i in range(n - 1):
#     fib.append(fib[-2] - fib[-1])
#
#
# fib.reverse()
#
# for i in range(n):
#     fib.append(fib[-1] + fib[-2])
#
# print(fib)
