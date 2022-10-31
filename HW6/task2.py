# Напишите программу, которая найдёт произведение пар чисел списка.
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

# Новое решение

from random import randint
my_list = [randint(-10, 10) for i in range(10)]
result_list = [my_list[i]*my_list[-i-1] for i in range((len(my_list)+1)//2)]
print(f'Исходный список: {my_list}\nРезультат: {result_list}')
