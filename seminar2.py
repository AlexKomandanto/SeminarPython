# a = 5
# b = 15
#
# a, b = b, a  # смена значений операторов

# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# - Для N = 5: 1, -3, 9, -27, 81

# def show_sequence(n):
#     for i in range(n):
#         num_ = (-3) ** i
#         print(num_, end=' ')
# num_ = int(input('Введите число: '))
# show_sequence(num_)


# 2. Для натурального n создать список, состоящий из элементов последовательности 3n + 1.
# - Для n = 6: [4, 7, 10, 13, 16, 19]

# def create_list(n):
#     temp = []
#     for i in range(1, n + 1):
#         temp.append((3 * i) + 1)
#     return temp
# numb = create_list(int(input('Enter n: ')))
# print(numb)


# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество
# вхождений одной строки в другой.
# ssabababsdaasd aba -> 2

# str1 = 'ssabababasdaasd'
# str2 = 'aba'
# length = len(str1) - len(str2)
# count = 0
# for i in range(length):
#     if str2 in str1[i:i + len(str2)]:
#         count += 1
# print(count)

