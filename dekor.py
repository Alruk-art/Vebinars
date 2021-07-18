# Part 1
from datetime import datetime

def one():
    start = datetime.now()
    l=[]
    for i in range(10**5):
        if i % 2 == 0:
            l.append(i)
    print(datetime.now()- start)
    return l
def two():
    start = datetime.now()
    l= [x for x in range(10**5) if x % 2 == 0]
    print(datetime.now() - start)
    return l

l1 = one()
l2 = two()
#print (l1)
#print (l2)

# Part 2
print ('part 2')
from datetime import datetime
def timeit(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print("timeit=",datetime.now() - start)
        return result
    return wrapper

@timeit
def one2():
    start = datetime.now()
    l=[]
    for i in range(10**5):
        if i % 2 == 0:
            l.append(i)
#    print(datetime.now()- start)
    return l

@timeit
def two2():
    start = datetime.now()
    l= [x for x in range(10**5) if x % 2 == 0]
#    print(datetime.now() - start)
    return l

l3 = one2()
l4 = two2()
n =10**5

# Part 3
print ('part 3')
from datetime import datetime
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print("timeit=",datetime.now() - start)
        return result
    return wrapper

@timeit
def one3(n):
    start = datetime.now()
    l=[]
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
#    print(datetime.now()- start)
    return l

@timeit
def two3(n):
    start = datetime.now()
    l= [x for x in range(n) if x % 2 == 0]
#    print(datetime.now() - start)
    return l

l5 = one3(n)
l6 = two3(n)

# Part 4
print ('part 4')
print (n)
from datetime import datetime
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print("timeit=",datetime.now() - start)
        return result
    return wrapper

@timeit
def one4(n):
    start = datetime.now()
    l=[]
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
#    print(datetime.now()- start)
    return l

@timeit
def two4(n):
    start = datetime.now()
    l= [x for x in range(n) if x % 2 == 0]
#    print(datetime.now() - start)
    return l

#l7 = one4
#a = l7(n)
#l8 = two4
#b = l8(n)
#print (n)
l9 = (one4)(n)
l10 = (two4)(n)

# Part 5
print ('part 5')
print (n)
from datetime import datetime
def timeit(arg):
    print(arg)
    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print("timeit=",datetime.now() - start)
            return result
        return wrapper
    return outer
@timeit('test one')
def one5(n):
    l=[]
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l

@timeit('test two')
def two5(n):
    l= [x for x in range(n) if x % 2 == 0]
    return l

l11 = timeit('test one5')(one5)(n)
l12 = timeit('test two5')(two5)(n)

