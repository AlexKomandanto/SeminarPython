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

# Новое решение

n = int(input('Укажите n: '))
res_list = [i for i in range(1, n+1) if n%i == 0]
print(res_list)

