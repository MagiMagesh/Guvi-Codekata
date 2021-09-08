def indices(n,array): #a = 85 96 84 25 13 36
    if n == len(array):
        o = dict()
        for i in array:
            o[int(i)] = array.index(i)   # {85:0, 96:1, 74:2, 25:3, 13:4, 36:5}
        s = sorted(o)               # {13,25,36,74,85,96}
        s.reverse()                 # {96,85,74,36,25,13}
        fo = []
        for v in s:
            fo.append(str(o[v]))         #fo = [1,0,2,5,3,4]
        print(' '.join(fo))
indices(int(input()),input().split())