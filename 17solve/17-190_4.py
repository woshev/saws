'''
Решение № 4. Михлин Б.С.
17.190 (П. Волгин) В файле 17-7.txt содержится последовательность целых чисел.
Элементы последовательности могут принимать значения от 0 до 200 включительно.
Рассматривается множество элементов последовательности, которые удовлетворяют следующему условию:
число в восьмеричной записи оканчивается на 7, но не оканчивается на 27.
Найдите количество таких чисел и максимальное из них.
'''
f = open('17-7.txt')
a = [int(x) for x in f if int(x)%8 == 7 and int(x)%64 != 23] # 27(8) = 23(10)
print(len(a),max(a)) # Ответ: 9 63
