l=("hello world computer yes").split()
#l=l.split();
#print(l)
llen=len(l)
a=set(l)
print (a)
print (l,llen)
for i in l:
    print (i, len(i))

l=("1 3 5 7 9").split()
print('"1 3 5 7 9" после split ', l)
l = list(range(21))
print (type(l))
l=list(map(int, l))
print (l)
print (type(l))
a=0
for i in l:
     i = int(i)
     a +=i
print ('сумма 21 = ', a)
print (type(a))

l = [1,2,3]
l2=[3,5,7]
print (l+l2)

l=[1,2,3,5,6]
l2=[2,3,4,4,6]
l3=l+l2
print ("set ",set(l3))
l={1,2,3,5,6}
l2={2,3,4,4,6}
l3=(l2.union(l))
print("union", l3)
print("diff",l2.difference(l))
print("inters",l2.intersection(l))

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
ans1 = math.sqrt(a**2 + b**2) # ищем гипотенузу
ans2 = (a**2 + b**2)**.5 # без библиотеки math
ans3 = math.hypot(a, b) # сразу вычисляем гипотенузу
print(ans1, ans2, ans3)
