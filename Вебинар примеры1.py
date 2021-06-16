# a, b = [int(input('через ввод: ')) for i in range(2)]
# print(a, b)
# a, b = map(int, input('через запятую: ').split(','))
# print(a, b)

at_index = None
em = "alruk@mail.ru"
for i in range(len(em)):
    if em[i] == '@':
        print(em[i + 1:])
        print(em[0: i])

print('через split ', em.split('@')[0], em.split('@')[-1])  # -1 усли несколько '@', то взять последний

print(em.find('@'))  # символ стоит на пятом месте
print('через Find ', em[em.find('@') + 1:])

s = em.index('@')
print('через index ', em[s + 1:])

A = ['hell', 1, 1, 2, '-2d', 'num', 'num', '-3', -3, 18, 3, 21, 21, 66, 23, 24, 33, 45, 121]

print(A)
A = [elem for elem in A if type(elem) == int] # ещё способ убрать не числа

#B = [] это старый способ убрать не числа
#for i in A :
    #if type(i) == int:
    # if str.isdigit(str(i)):# ищет не числа и числа меньше 0, alpha удалет только слова
        #B.append(i) # формируем новый список
        # print(i, end = ',')
#A = B
print('удаляем не числа ', A)

A = list(set(A))
print ('Убираем дубликаты', A)

A=sorted(A)
print('Сортируем ',A)
s = []
for i in range(len(A)):
    if A[i] % 3 == 0:  # делятся на три
        s.append(A[i])
print('числа делятся на три ', s)

s=[]
for i, elemt in enumerate(A):
    if elemt % 3:
        s.append(elemt)
print('метод enumerate, числа НЕ делятся на три ', s)

s = sum(elemt for i, elemt in enumerate(A) if elemt % 3 == 0)
print(s)

print ('сдвиг элементов через pop, последний перемещаем на в начало')
last = A.pop()
A.insert(0, last)
print(A)

print ('сдвиг элементов через срез')
n = 2 # сколько элементов взять с конца и вставить в начало списка. чтобы n не было больше длины списка
A = A[-n:]+A[:-n]
print(A)
print()

A = [1, 1, 2, 2, 3, 4, 5, 5, 6]
print('Дан новый список ', A)
# A = list(set(A)) # 'Убираем все дубликаты'
min_elemt = None
for elemt in A:
    if min_elemt == None or min_elemt > elemt:
        min_elemt = elemt
print('миним элементв в списке А = ', min_elemt)

# вывести второй и третий минимум
# первый способ
A = [1, 1, 2, 2, 3, 4, 5, 5, 6]
first_min = A.pop(A.index(min(A)))
A = list(filter(lambda elem: elem != first_min, A)) # убираем дубликат первого минимума
second_min = A.pop(A.index(min(A)))
third_min = A.pop(A.index(min(A)))
print('второй и третий мин в списке ', second_min, third_min)
print('что осталось ',A)
# второй способ
print()
A = [1, 1, 2, 1, 2, 2, 2, 3, 4, 5, 5, 6]
# print('Дан новый список ', A)
first_min1 = min(A)
print(min(A))
A.remove(first_min1)
print(A)

# A = list(filter(lambda elem: elem != first_min1, A)) # убираем дубликат первого минимума
A = [elem for elem in A if elem != first_min1] # создаём новый список
print('del 1W = ',A)
second_min = min(A)
A.remove(second_min)
third_min = min(A)
A.remove(third_min)
print('второй и третий мин в списке ', second_min, third_min)
print('что осталось ',A)


A = [1,  5,  2,  6,  3, 4,  6]
print('Метод sort ', A)
A.sort()
print('Выводим второй и третий мин', A[1], A[2])
#import heapq метод куча читать отдельно


print('Задача 7')
# ввести число с клавиатуры, затем число n в n-ичной системе оно записано. И это число вывести в десятичной системе.
s = '1101'
n = 3 # симеричная система
print ('число ', s, 'в системе ', n)
ans = 0
for i in range(len(s)):
    ans *= n
    ans += int(s[i])
print('число ',s, ' в 10-ной системе = ', ans)

print ('второй способ')
ans = 0
for i in s:
    ans *= n
    ans += int(i)
print('число ',s, ' в 10-ной системе = ', ans)

print ('третий способ')
ans = int(s, n) # это специал функция для перевода из одной системы в другую
print('число ',s, ' в 10-ной системе = ', ans)

print('Задача 7 склеивание списков')

A = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10], [11], [12, 13, 14]]
B = []
for elem in A:
    for i in elem:
        B.append(i)
print('новый список ',B)
print ('Второй способ B.extend(elem) ')
B = []
for elem in A:
    B.extend(elem)
print('новый список ',B)

print ('третий способ B += elem ')
B = []
for elem in A:
    B += elem
print('новый список ',B)

print ('четвёртый способ sum(A, []) ')
B = sum(A, [])
print('новый список ',B)