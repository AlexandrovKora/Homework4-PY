"""Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств
"""
"""
n = int(input("Введите кол-во эл-тов 1 множества: "))
m = int(input("Введите кол-во эл-тов 2 множества: "))

count = 0
count_m = 0
list_n = []
list_m = []
while count < n:
    list_n.append(int(input(f'Введите значение {count + 1} элемента из 1 множества: ')))
    count += 1
print()
while count_m < m:
    list_m.append(int(input(f'Введите значение {count_m + 1} элемента из 2 множества: ')))
    count_m += 1

set_n = set(list_n)
print(f'Первое множество: {set_n}')

set_m = set(list_m)
print(f'Второе множество: {set_m}')

intersec = set_n.intersection(set_m)

list_result = list(intersec)
k = 0
for j in range(len(list_result)):
    for i in range (len(list_result)-1):
        if list_result [i] > list_result [i+1]:
            k = list_result [i]  
            list_result[i] = list_result [i+1]
            list_result [i+1]=k

print(list_result)
"""


'''Задача 24: В фермерском хозяйстве в Карелии выращивают 
чернику. Она растет на круглой грядке, причем кусты высажены 
только по окружности. Таким образом, у каждого куста есть ровно 
два соседних. Всего на грядке растет N кустов. Эти кусты 
обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.

В этом фермерском хозяйстве внедрена система автоматического 
cбора черники.
Эта система состоит из управляющего модуля и нескольких 
собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно 
перед некоторым кустом, собирает ягоды с этого куста и с двух 
соседних с ним.
Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, находясь 
перед некоторым кустом заданной во входном файле грядки.'''

"""

bushes = int(input("Введите кол-во кустов: "))
count = 0
list_berries = []
while count < bushes:
    list_berries.append(int(input(f'Введите количество ягод на {count+1} кусте: ')))
    count += 1

print(list_berries)
i = 0

result = []

while i < bushes:
    if i == bushes - 1:
        sum = list_berries[i] + list_berries[i - 1] + list_berries[0]
    else:
        sum = list_berries[i] + list_berries[i - 1] + list_berries[i + 1]
        result.append(sum)
        result.sort()
    i += 1

print(f'Максимальное число ягод за один заход: {result[-1]}')
"""