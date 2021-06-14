# a=int(input('Введите число :'))
a = '12345'
digs = str(a)
s= sum(map(int,digs))
print(s)
s = 0
for digs in str(a):
    s += int(digs)
print(s)

import math
a = 3
b = 6
ans = math.sqrt(a**2 + b**2) # ищем гипотенузу
print(ans)