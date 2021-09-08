def rearrange(n, array):
    if n == len(array):
        o = []
        o2 = []
        for i in array:
            o.append((int(i)))
        for j in range(n):
            b =  o[o[j]]
            o2.append(str(b))
        print(' '.join(o2))

rearrange(int(input()), input().split())