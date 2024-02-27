c=0
mx=0
mi=0
for i in range(3721,7753):
    '''s=0
    n=i
    while n>0:
        s+=n%10
        n//=10'''
    s=0
    for j in str(i):
        s+=int(j)
    if s%3==0 and i%8!=0:
        if mi==0:
            mi=i
        c+=1
print(c,mi)
