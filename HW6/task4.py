#Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


# n = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
#
# result = []
# for i in n:
#     if i in result:
#         continue
#     elif n.count(i) == 1:
#         result.append(i)
# print(f'Исходный список: {n}')
# print(f'Список неповторяющихся элементов: {result}')

# Новое решение

my_list = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
print(f'Исходный список: {my_list}\nСписок неповторяющихся элементов: {list(filter(lambda i: my_list.count(i) ==1, my_list))}')