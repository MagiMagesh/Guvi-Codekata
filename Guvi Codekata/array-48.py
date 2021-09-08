a = input().split()
array2 = input().split()
array1 = []
o = dict()
count = 1
for i in a:
    array1.append(int(i))
l = array1[0]
while l > 0:
    if array1[1] == len(array2):
        a2 = []
        for i in array2:
            a2.append(int(i))
        for j in a2:
            if j == 0:
                i = 'RAM'
            else:
                i = 'SITA'
                if i not in o:
                    o[i] = count
                else:
                    o[i] = o[i] + count
    l= l-1
for i in o.items():
    print(i)


