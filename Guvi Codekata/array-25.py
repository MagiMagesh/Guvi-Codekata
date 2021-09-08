def loe(n, array):  # array = 9 6 1 2 9 6 5 1 8
    if n == len(array):
        o = dict()
        count = 1
        for i in array:
            if i not in o:
                o[i] = count
            else:
                o[i] = o[i] + count
        # o = {'9':2,'6':2,'1':2,'2':1,'5':1,'8':1}
        o1 = []
        for w, c in o.items():
            if c == 1:
                o1.append((w))  # o1= [2,5,8]
            elif c == len(array):
                o1.append((w))
        b = sorted(o1)
        b.reverse()
        print(' '.join(b))

loe(int(input()), (input()).split(' '))