

# print('x y z \t¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
# for n in range(64):
#     n = bin(n)[2:].rjust(6, '0')
#     print(n)
# # x, y, z = int(n[0]), int(n[1]), int(n[2])
# # print(x, y, z, '\t', not(x or y or z) == (not(x) and not(y) and not(z)))


# print('x y z \t¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
# for n in range(8):
#     n = bin(n)[2:].rjust(3, '0')
#     print(n)
# # x, y, z = int(n[0]), int(n[1]), int(n[2])
# # print(x, y, z, '\t', not(x or y or z) == (not(x) and not(y) and not(z)))


# 1. Напишите программу, которая определит
# позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# a = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
#
# value = "qwe"
# j = 0
#
# for i in range(len(a)):
#     if a[i] == value:
#         j = j + 1
#     if j == 2:
#         print(i)
#         break


# 2. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.
# '''["123", "234", 123, "567", 'werwer', 33, '324', 'werwww']

# a = ["123", "234", 123, "567", 'werwer', 33, '324', 'werwww']
# value = 12
#
#
# for i in range(len(a)):
#     if type(a[i]) == int:
#         if a[i] == value:
#             print(f' Value found on position {i}')
#             break
#     elif type(a[i]) == str:
#         if a[i].isdigit() and int(a[i]) == value:
#             print(f' Value found on position {i}')
#             break
# else:
#     print('Value not found')


r = int(input('Введите длину массива: '))
list_ = []
print('Введите элементы массива, таким колличеством элеменнтов -> ', r)
for i in range(r):
    num = input()
    list_.append(num)
# print(list_)
find = int(input('Введите значение для поиска: '))
for i in range(len(list_)):
    if list_[i].isdigit() and find == int(list_[i]):
        print(f'Значение <<{find}>> имеет индекс -> {i} ')
        break
else:
    print(f'Значение <<{find}>> не найдено в массиве -> {list_}')

