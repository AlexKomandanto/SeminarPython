# with open('new_file', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     # print(1, f.readline())
#
# print(lines)
# lines[3] = 'Hello!!\n'
#
# with open('new_file', 'w', encoding='utf-8') as f:
#     for line in lines:
#         f.write(line)


# mem = {1: 1, 2: 1}        # Менее затратный для памяти, метод выполнения операции
#
#
# def fib(n):
# if n not in mem:
# mem[n] = fib(n - 1) + fib(n - 2)
# return mem[n]
#
#
# print(fib(405))


# 1. Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# nums = list(map(int, input('Enter : ').split()))
# nums.sort()
# print(nums[0], nums[- 1])


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0
# с помощью математических формул нахождения корней квадратного уравнения

# a,b,c = list(map(int, input('Enter : ').split()))
# if a != 0 and (b**2 - 4 * a * c) >= 0:
#     x1 = (-b - (b**2 - 4 * a * c)**0.5) / (2*a)
#     x2 = (-b + (b**2 - 4 * a * c)**0.5) / (2*a)
#     print(x1, x2)
# else:
#     print('Корней нет')


# 3. Задайте два числа. Напишите программу,
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# print(a)

# a, b = list(map(int, input('Enter : ').split()))
# for i in range(2, min(a, b) + 1):
#     if a % i == 0 and b % 1 == 0:
#         print(i)
#         break
# else:
#     print('нет общего делителя')


# a, b = list(map(int, input('Enter : ').split()))
# for i in range(min(a, b) + 1, 1, -1):
#     if a % i == 0 and b % 1 == 0:
#         print(i)
#         break
# else:
#     print('нет наименьшего общего кратного')





