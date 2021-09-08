def merge(n, array1, array2):  # n = 4    :::::  a1 = 1 2 3 4 ::::: a2 = 5 6 7 8
    if n == len(array1) and n == len(array2):
        for i in array1:
            array2.append(i)  # a1 = ['1','2','3' ,'4' ,'5' ,'6' ,'7' ,'8']
        o2 = []
        for i in array2:
            o2.append(int(i))  # o2 = [1,2,3,4,5,6,7,8]
        o = sorted(o2)
        if len(o) % 2 == 0:
            m = len(o) // 2
            o1 = o[m - 1] + o[m]
        elif len(o) % 2 != 0:
            m = -(-len(0) // 2)
            o1 = m
        print(o1)


merge(int(input()), input().split(' '), input().split(' '))
