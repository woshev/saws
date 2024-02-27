data = [int(x) for x in open("17-324.txt")]
N = len(data)

spec = [ x for x in data if x % 31 == 0 ]
M = sum(spec) / len(spec)

def isPalindrome( n, base = 10 ):
  s = ''
  n0 = n
  while n:
    s = str(n%base) + s
    n //= base
  return s == s[::-1]

def valid( a, b, c ):
  return isPalindrome(a+b+c, 5) and \
         (a + b + c) / 3 > M

count, mi = 0, None
for i in range(N-2):
   s = sum( data[i:i+3] )
   if valid( data[i], data[i+1], data[i+2] ):
     count += 1
     if mi == None or s < mi:
       mi = s

print( count, mi )

