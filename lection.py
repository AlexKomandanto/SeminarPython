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


def f(x):
    return x**2
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2.3
print(f(arg))
print(type(f(arg)))

# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) # NoneType