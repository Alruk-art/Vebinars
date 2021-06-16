def func1():
    3 + 5


def func2():
    return 3 + 5


def func3(a):
    return a + 5


def func4(a, b):
    return a * b


print(func1())
print(func2())
print(func3(3))
print(func4(3, 5))
var1 = func2
var2 = func2()
var3 = func3(6)
var4 = func4(6, 8)
print('var1= ', func2)
print('var2=(3+5)= ', func2())
print('var3=(6+5)= ', var3)
print('var4=(6*8)= ', var4)

print('-' * 25)


# Проверка ввода имени, затем проверка возраста
def person(mname, age):
    if age > 18:
        age = '>18'
    else:
        # age = '<18'
        return
    mname = str.upper(mname)  # все символы с большой буквы
    print((f'My name is {mname})', (f'my age is {age}')))


def chname(mname):
    mname = str.isalpha(mname)  # проверка, что в имени нет цифр
    return mname


def cha(age):  # проверка на число
    try:
        int(age)
        return True
    except ValueError:
        return False


# ввод данных
while type:
    # mname = input('name: ')
    mname = 'egor'
    if chname(mname):  # проверка на цифры в имени
        print('Правильно, имя из букв')
        while type:
            # age = input('age: ')
            age = '33'
            if cha(age) is False:
                print('это не число')
            else:
                age = int(age)
                person(mname, age)
                if age < 18:
                    print('age is < 18')  # повторный запрос возраста
                else:
                    break
        l = 1  # просто так
        if l == 1:
            print('Yes')
            break
    else:
        print('в имени должны быть только буквы')
        for i in mname:
            if str.isalpha(str(i)):
                pass
            else:
                print('ошибка ввода, это не буква алфавита', (list(mname[i])))

print('*' * 25)

a = [1, 2, 3]
b = [*a, 5, 6]
print(a, b)
a = [3, 2, 1]
print(a, b)


def unknow(*args):
    print(type(args))
    for argument in args:
        print(argument)


unknow('hello', 'world', 'people')
unknow((1, 3, 4, 2, '7', 5))


def list_market(**products):
    print(type(products))
    reserv = 250
    for prod, ostk in products.items():
        print('Товар - ', prod, 'остаток - ', ostk, end="")
        if (type(ostk)) == int and ostk < reserv:
            print(', он заканчивается ! ', end="")
        print()


list_market(помидоры=200, огурцы=70, шоколадки=[50, 25, 40], перец=300)
print('+' * 25)

num_strings = ['10', '1', '.75', '4.2']
print(list(map(float, num_strings)))

[float(i) for i in num_strings]

myfunc = lambda x, y: x + y
print(myfunc(1, 3))
print((myfunc('a, ', 'b, ')))
mf = myfunc([100, 'помидор'], [200, 'огурец'])
print(mf)
print((mf[1], mf[3]))
myfunc = lambda x, y, z: x + y + z
mf = myfunc([100, 'помидор', 50], [200, 'огурец', 75], [300, 'перец', 125])
print(mf)
print(mf[1], mf[4], mf[7])

y = (lambda x: x ** 2)(8)
print('8**2= ', y)

myfunc = lambda x, y: x + y if x % 2 != 0 else 0  # усли х чётный, то считаем x+y иначе ноль.
print(myfunc(1, 2))
print(myfunc(0, 2))


def mname(*x):
    return sum(x)


mname2 = lambda *x: sum(x)

sss = [1, 2, 3, 4, 5]
print('mname1= ', mname(*sss))

print('mname2= ', mname2(1, 2, 3, 4, 5))

print('Функция фильтр')
x = 5
nums = [1.0, 21.0, 30.0, 33.4, 12.0, 5.1]
print(sorted(list(filter(lambda x: x < 30, nums))))
print(max(list(filter(lambda x: x < 30, nums))))


def odd_num(x):
    return x % 3 == 0 # те числа, что делятся на три без остатка.

print(sorted(list(filter(odd_num, nums))))

print('ООП объектно-ориентированное программирование')

number = 3.5
print (number.__class__)

new_string = 'akskkd'
print(new_string.replace('k', 'z'))

my_list = [2,6,7,12,4]

print(sorted((my_list)))
print(my_list) # ничего не изменилось
print(my_list.__class__)
my_list.sort() # изменяется класс my_list
print(my_list) # отсортированный список

print ('*** Классы ***')
class FootballClub:
    pass
Ivanov = FootballClub()
Ivanov.name = 'Ivanov'
Ivanov.goals = 5
print (type(Ivanov))
print(Ivanov.name, Ivanov.goals)
print ('Футбольная команда')
class FootballClub:
    squad = {}
    def __init__(self, name, goals = 0, captain = False, assists=0):
        self.name = name
        self.goals = goals
        self.captain = captain
        self.assists = assists
        #FootballClub.squad[self.name] = self.goals
        #FootballClub.squad[self.name] = self.assists
        #FootballClub.squad[self.name] = self.captain
    def scored(self, goals):
        self.goals += goals
        FootballClub.squad[self.name] = self.goals, self.captain, self.assists

Ivanov = FootballClub('Ivanov', assists=2)
Petrov = FootballClub('Petrov', captain=True, assists=1)
# голы считаем отдельно
Ivanov.scored(2)
Petrov.scored(3)
Petrov.scored(4) # мячи суммируются
print(type(FootballClub.squad))
print(FootballClub.squad)
print (list(FootballClub.squad.keys()))
print ((FootballClub.squad.items()))