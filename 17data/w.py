array = []
with open('17-1.txt') as f:
    for i in f.readlines():
        array.append(int(i))

c = 0
m = -20000
for i in range(1, len(array) - 1):
    if array[i - 1] > array[i] < array[i + 1]:
        c += 1
        m = max(m, array[i])
print(c, m)
