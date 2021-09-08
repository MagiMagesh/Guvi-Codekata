a = int(input(''))
b = input('')
c = b.split()
value = []
for i in c:
    value.append(int(i))
values = value.sort()
#print(value)
for i in value:
    print(i , end = ' ')