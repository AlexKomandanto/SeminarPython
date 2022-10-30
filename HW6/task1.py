
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# list_all_inn = map(int, a, b)
# print(list_all_inn)
# list_all_inn = list(map(lambda x: a[x] == b[x], list_all_inn))
#
# print(list_all_inn)

result = list(filter(lambda elem: elem in b, a))

print(result)
