def kelements(array1,array2):
    o = []
    for i in array1:
        o.append(int(i))
    print(o)
    if o[0]== len(array2):
        b = o[1]
        c = len(array2)
        d = (c-b)
        print(d)
        g =[]
        fo=[]
        g.append(str((array2[:d])))
        for i in g:
            fo.append(i)
        print(' '.join(fo))
kelements(input().split(' '), input().split(' '))