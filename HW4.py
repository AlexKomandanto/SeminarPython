# Вычислить число π c заданной точностью d
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# from math import pi
#
# dict_pi = {}
# # d = 1
# d = input('Enter d: ')
# for d in range(1, 11):
#     value = round(pi, d)
#     dict_pi[d] = value
# print(dict_pi)

# 2 Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# - при N=236     ->        [2, 2, 59]

# n = int(input('Enter n: '))
#
# nums_n = []
# k = 2
# while n != 1:
#     if n%k == 0:
#         nums_n.append(k)
#         n //= k
#     else:
#         k += 1
# print(nums_n)

# 3 Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

# n = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
#
# result = []
# for i in n:
#     if i in result:
#         continue
#     elif n.count(i) == 1:
#         result.append(i)
# print(result)


# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0




# 5 Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.