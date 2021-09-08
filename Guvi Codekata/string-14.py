def sum(array):
    a = []
    s = []
    for i in array:
        try:
            val = int(i)
            if val > 0:
                s.append(val)
        except:
            a.append(i)
    print(s)
    sum = 0
    for v in s:
        sum = v + sum
    print(sum)
    a.append(str(sum))
    print(''.join(a))


sum(input())
