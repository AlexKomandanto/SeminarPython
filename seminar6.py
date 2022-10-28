# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# 1 вариант решения
s = '10*55+21*2'

lst = []
last = -1
for i in range(len(s)):
    if s[i] in {'+', '-', '*', '/'}:
        lst.append(s[last + 1:i])
        lst.append(s[i])
        last = i
lst.append(s[last + 1])
print(lst)

s = lst

lst_res = [int(s[0])]
i = 1
while i < len(s):
    if s[i] == '+':
        lst_res.append(int(s[i + 1]))
    elif s[i] == '-':
        lst_res.append(-int(s[i + 1]))
    elif s[i] == '*':
        lst_res[-1] = lst_res[-1] * int(s[i + 1])
    elif s[i] == '/':
        lst_res[-1] = lst_res[-1] / int(s[i + 1])
    i += 2

print(lst_res)
print(sum(lst_res))

                    # 2 вариант решения через рекурсию
# def ex_1():
#     def get_dict_from_polinom(str_pol):
#         lst = []
#         last_index = -1
#         neg = False
#         for i, char in enumerate(str_pol):
#             if char == '+' or char == '-':
#                 if neg:
#                     lst.append('-' + str_pol[last_index + 1:i])
#                 else:
#                     lst.append(str_pol[last_index + 1:i])
#                 last_index = i
#                 neg = char == '-'
#         if neg:
#             lst.append('-' + str_pol[last_index + 1:])
#         else:
#             lst.append(str_pol[last_index + 1:])
#         return lst
#
#     lst = get_dict_from_polinom("1-22*33")
#     print(lst)
#     sums_2 = 0
#     for i in lst:
#         if "*" in i or "/" in i:
#             prods = i.split("*")
#             prod = 1
#             for char in prods:
#                 if "/" in char:
#                     dels = char.split("/")
#                     r = int(dels[0])
#                     for k in range(1, len(dels)):
#                         r /= int(dels[k])
#                 else:
#                     r = int(char)
#                 prod *= r
#             sums_2 += prod
#         else:
#             sums_2 += int(i)
#     print(sums_2)
#
#
# ex_1()
# 2 Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;




# 3. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]



