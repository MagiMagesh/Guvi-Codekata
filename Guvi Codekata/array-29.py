
def user(n):
    o = []
    while n >0:
        n = n-1
        o.append(input())
    o1 = []
    print(o)
    a =0
    while a<int(n):
        b = o[a].split(' ')
        if b[a][0]==1:
            o1.append(int(b[a][1]))
        elif b[a][1] ==0:
            o1.append(-1)
        a = a +1
    print(o1)
user(6)


def user(n,a1,a2,a3,a4,a5):
    o =[]
    o1=[]
    o.append(int(a1[1]))
    if a2[0]== '2':
        o1.append(int(a1[1]))
    o.append((int(a3[1])))
    if a4[0]=='2':
        o1.append(int(a3[1]))
    b = sorted(o1)
    b.reverse()
    fo=[]
    for i in b:
        fo.append(str(i))
    print(' '.join(fo))

user(int(input()),input().split(' '),input().split(' '),input().split(' '),input().split(' '),input().split(' '))

