# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint
#
# n = int(input('Укажите размер списка: '))
# min = int(input('Введите минимальное значение диапазона: '))
# max = int(input('Введите максимальное значение диапазона: '))
# summ_nums = 0
# my_list = []
#
# for i in range(n):
#     my_list.append(randint(min, max))
# print(my_list)
#
# for index in range(len(my_list)):
#     if index%2==1:
#         summ_nums+=my_list[index]
# print(summ_nums)

# Новое решение


print(sum(list(map(int, input('Введите значения списка: ').split(',')))[1::2]))
