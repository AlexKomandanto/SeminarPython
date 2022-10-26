
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Создайте программу для игры с конфетами человек против человека.

with open("file_task1", "w", encoding="UTF-8") as data_file:
    data_file.write("1 2 3 4 5 7 8 9")                      # создали файл и записали в него данные
with open("file_task1", "r", encoding="UTF-8") as data_file:
    string = data_file.readline()                            # открыли файл и прочитали с него данные
string = list(map(int, string.split()))             # сохранили в переменную данные и перевели их численные инт
a = 0
for i in range(1, len(string)):
    if string[i] - 1 != string[i - 1]:               # прошли 1й список по элемента и сравнили со 2м
        a = i


print(string[a]-1)           # вывели полученное значение

