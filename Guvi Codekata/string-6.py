def wonder(user):
    c = dict()
    count=0
    for i in user:
        if i not in c:
            c[i] = count+1
        else:
            c[i] = c[i] + count
    if len(c) ==3:
        print('Wonder')
    else:
        print('-1')
wonder(input(''))