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

# import random
# import itertools
#
# k = int(input('Задайте натуральную степень k: '))
# koeffs_lst = []
#
# koeffs_list = list([random.randint(0, 101) for i in range(k + 1)])
# if koeffs_list[0] == 0:
#     koeffs_list[0] = random.randint(1, 101)
# print(f' Список коэффициентов: {koeffs_list}')
#
#
# def get_polynomial(k, koeffs_list):
#     str1 = ['*x**'] * (k - 1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(koeffs_list, str1, range(k, 1, -1), fillvalue='') if
#                   a != 0]
#
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x', ' x')
#
#
# list = get_polynomial(k, koeffs_list)
# print(list)
#
# with open('Poly.txt', 'w') as data:
#     data.write(list)

# 5 Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.

from itertools import chain
import itertools
import re

file1 = 'text.txt'
file2 = 'text2.txt'
file_sum = 'sum.txt'


def read_file(file):
    with open(str(file), 'r') as data:
        text = data.read()
        return text


def convert_file(text):
    text = text.replace("= 0", "")
    text = re.sub("[*|^| ]", " ", text).split("+")
    text = [char.split(' ') for char in text]
    text = [[x for x in list if x] for list in text]
    for i in text:
        if i[0] == "x":
            i.insert(0, 1)
        if i[-1] == "x":
            i.append(1)
        if len(i) == 1:
            i.append(0)
    text = [tuple(int(x) for x in j if x != "x") for j in text]
    return text


def fold_text(text1, text2):
    x = [0] * (max(text1[0][1], text2[0][1] + 1))
    for i in text1 + text2:
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key=lambda r: r[1], reverse=True)
    return res


def get_sum(text):
    var = ['*x^'] * len(text)
    coefs = [x[0] for x in text]
    degrees = [x[1] for x in text]
    new_text = [[str(a), str(b), str(c)]
                for a, b, c in (zip(coefs, var, degrees))]
    for x in new_text:
        if x[0] == '0':
            del (x[0])
        if x[-1] == '0':
            del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == ' *x^':
            del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1':
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_text = list(itertools.chain(*new_text))
    new_text[-1] = ' = 0'
    return "".join(map(str, new_text))


def write_to_file(file, text):
    with open(file, 'w') as data:
        data.write(text)


text1 = read_file(file1)
text2 = read_file(file2)
text1_1 = convert_file(text1)
text1_2 = convert_file(text2)

text_sum = get_sum(fold_text(text1_1, text1_2))
write_to_file(file_sum, text_sum)

print(text1)
print(text2)
print()
print(text_sum)
