### GOT THE RIGHT CODE AFTER LOT OF TRIALS USING PYCHARM
### BUT HAVE TO TRY WITHOUT AND IDE

def mirror(n):
    v = []
    for i in range(n):
        v.append(input().split())
    o = []
    for i in range(1, len(v)):
        for j in range(0, i):
            if v[j][j] == v[i][i] and v[j][i] == v[i][j]:
                print('YES')
                break
            else:
                print('NO')
                exit()

mirror(int(input()))

##### THE ABOVE IS RIGHT CODE



# almost wright need some improvement

def mirror(n):
    v = []
    for i in range(n):
        v.append(input().split())
    o = []
    for i in range(1, len(v)):
        for j in range(0, i):
            try:
                if v[j][1] == v[i][0] or v[i][0] == v[j][1]:
                    print('YES')
                    break
            except:
                print('NO')
                exit()

mirror(int(input()))




def mirror(n):
    v = []
    for i in range(n):
        v.append(input().split())
    for i in range(1, len(v)):
        for j in range(0, i):
            if v[j] == v[i]:
                print('yes')


mirror(int(input()))



def mirror(n):
    v = []
    for i in range(n):
        v.append(input().split())
    for i in range(1, len(v)):
        for j in range(0, i):
            if v[j] == v[i]:
                print('yes')


mirror(int(input()))




def mirror(n, a1, a2, a3):
    if a1[0][1] == a2[1][0] or a1[0][1] == a3[1][0]:
        print('YES')
    else:
        print('NO')


mirror(int(input()), input().split(), input().split(), input().split())

