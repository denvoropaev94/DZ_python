# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

n = int(input("Введите количество элементов: "))
spisok = []
sum = 0
for i in range(n):
    spisok.append(int(input(f'Введите {i + 1} элемент ')))
    if i%2!=0:
        sum+=spisok[i]
print(f'Список элементов - {spisok},\nСумма на нечётных позициях - {sum}')