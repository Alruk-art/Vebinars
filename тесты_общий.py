text = input('wait: ')
values = text.split(' ')
print (values[0])
print (values)
if len(values) == 2:
    values.insert(0, '1')
print (values)