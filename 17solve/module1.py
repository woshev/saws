from random import randint

N = 50000
D = 117
with open('17-338.txt','w') as F:
   mi = 115
   for i in range(N):
      if randint(0, 10000) == 0:
        n = mi
      elif randint(0, 5) == 0:
        n = D*randint(1,900) + mi
      else:
        n = randint(mi, 100000)
      if n <= 100000:
        print( n, file=F )

