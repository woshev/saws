'''
Решение № 2. Михлин Б.С.
17.190 (П. Волгин) В файле 17-7.txt содержится последовательность целых чисел.
Элементы последовательности могут принимать значения от 0 до 200 включительно.
Рассматривается множество элементов последовательности, которые удовлетворяют следующему условию:
число в восьмеричной записи оканчивается на 7, но не оканчивается на 27.
Найдите количество таких чисел и максимальное из них.
'''
f = open('17-7.txt')
a = [int(x) for x in f]
b = [x for x in a if x%8 == 7 and x%64 != 0o27]
print(len(b),max(b)) # Ответ: 9 63
