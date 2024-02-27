count = 0
maks = 0
for i in range(1012, 9638 + 1):
    if i % 3 == 0 and (i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0):
        count += 1
        maks = i
print(count, maks)
