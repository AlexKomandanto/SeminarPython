# print('hello world')


# типы данных и переменные
# int, float, boolean, str, list, None

# value = None
# a = 123
# b = 1.23
# print(type(value))
# print(type(a))
# print(type(b))
# value = 12345
# print(type(value))

# s = 'hello \nworld' - перенос строки
# s = 'hello world'
# print(s)  # вывод строки

# print(a,'-' ,b,'-' ,s)
# print('{1} - {2} - {0}'.format(a,b,s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = ['1', '2', '3', 'hello',]
# print(list)

#  Ввод и вывод данных  print/input
# print('Введите a: ')
# a = int(input())
# print('Введите b: ')
# b = int(input())
# print(a, ' + ' ,b, ' = ', a+b )
# print('{} - {}'.format(a,b))
# print(f'{a} - {b}')

# Арифметические операции
# +, -,*, /, %, //,**
# **, ⊕, ⊖,*, /, //, %, +, -
# ( ) Скобки меняют приоритет

# a = 1.3123
# b = 3
# c = round(a * b,3) # функция роунд вывод значений и колличество после запятой
# print(c)

# a = 3
# a += 5 # = a = a + 5

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |,
# ^
# Кое-что ещё: is, is not, in, not in

# a = 1 < 4 and 5 > 2
# print(a) #  сравнение FALSE and TRUE

# a = int(input('a = '))
# b = int(input('b = '))

# if a > b:
#     print(a)
# else:
#     print(b)


# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
#  print(inverted)
# Пожалуй
# хватит )
# 32

# Управляющие конструкции: for

# for i in 1, -2, 3, 14, 5:
# print(i**2) демонстрация квадратов чисел

# Знакомьтесь – range
# r = range(5) # range(0, 5)
# r = range(2, 5) # range(2, 5)
# r = range(-5, 0) # range(-5, 0)
# r = range(1, 10, 2) # range(1, 10, 2) показывает нечетные числа от 1 до 10
# r = range(100, 0, -20) # range(100, 0, -20)

# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#  print(i)
# # 100 80 60 40 20
# for i in range(5):
#  print(i)
# # 0 1 2 3 4


# Немного о строках

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#  print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# Списки: введение
# Список – пронумерованная, изменяемая коллекция
# объектов произвольных типов 

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# ran = range(1, 6) 
# print(type(ran))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(ran)
# print(type(numbers))
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]


# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# Функции
# Это фрагмент программы, используемый
# многократно

# from ast import arg


# def function_name(x):
# body line 1
# . . .
# body line n
# optional return


# def f(x):
#     return x**2
# def f(x):
#     if x == 1:
#         return 'Целое'      # можно сделать перенос в другую папку с кодом с помощью
#     elif x == 2.3:          # import lection as l ; print(l.f(1))
#         return 23
#     else:
#         return
#
# arg = 2.3
# print(f(arg))
# print(type(f(arg)))

# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) # NoneType


# Файлы
# Хранение данных
# Передача данных в клиент-серверных проектах
# Хранение конфигов
# Логирование действий


# Файлы
# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+


# with open('file.txt', 'a') as data:
#  data.write('line 1\n')
#  data.write('line 2\n')
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#  print(line)
# data.close()

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors)   # разделителей не будет
# data.write('\nline 2\n')    # разделителей не будет
# data.write('line 3\n')
# data.close()
# exit()

# def f(x):
#  return x**2
#
#
# def f(x):
#  if x == 1:
#  return 'Целое'
#  elif x == 2.3:
#  return 23
#  else:
#  return

# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) # NoneType


# def concatenatio(*params):
#     res: int = 0
#     for item in params:
#         res += item
#     return res


# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(concatenatio(1, 2, 3, 4))  # TypeError: ...


#  Рекурсия

# def fib(n):   # числа фибоначе
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)  # 1 1 2 3 5 8 13 21 34


# Кортежи
# Кортеж – это неизменяемый “список”

# a = (3, 4)
# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#  print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support
# item assignment


# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue


# Словари
# Неупорядоченные коллекции произвольных
# объектов с доступом по ключу


# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',                  # 1 значение ключи - 2 значение ключей
#         'left': '←',                #     keys()                values()
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])  # ←
# типы ключей могут отличаться


# for k in dictionary.keys():  # значения ключей
#     print(k)
# for k in dictionary.values():   # значения
#     print(k)
# for v in dictionary.values():   # все значения
#     print(v)


# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# # print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#  print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

# Множества
# Неупорядоченная совокупность элементов

# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set
#
# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')  # добавление в множества
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')    # удаление
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok  # исключение
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }    # очистка
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}  #обьединение
# i = a.intersection(b) # i = {8, 2, 5}  # пересечение
# dl = a.difference(b) # dl = {1, 3}      # отличие
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# {1, 21, 3, 13}

# s = frozenset(a)

list1 = [1, 2, 3, 4, 5]
# list2 = list1
#
# list1[0] = 123
# list2[2] = 333
#
# for e in list1:
#  print(e)
#
# print()
#
# for e in list2:
#  print(e)

# print(len(list1))
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# print(list1.pop(2)) # удаление индекса из списка(по умолчанию стоит последний)
# print(list1)

# print(list1.insert(2, 11)) # добавление индекса в список(позиция, обьект)
# print(list1)

print(list1.append(11)) # добавление индекса в конец списка(обьект)
print(list1)

