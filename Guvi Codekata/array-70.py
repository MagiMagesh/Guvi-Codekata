def first(n,array1):
    a = dict()
    count = 1
    for i in array1:
        if i not in a:
            a[i]= count
        else:
            a[i] = a[i]+count
    bigcount = None
    bigword = None
    for w,c in a.items():
        if bigcount is None or c > bigcount:
            bigword = w
    print(bigword)
first(int(input()),input().split(' '))