# yield
def gen_cd(n):
    while n !=-1:
        yield n
        n -= 1

#for i in gen_cd(4):
#    print (i)

# standrt
def cd(n):
    result = []
    while n != -1:
        result.append(n)
        n -= 1
    return result
#print (cd(4))

