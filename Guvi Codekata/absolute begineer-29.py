def seperation(user):
    o = []
    o1 =[]
    for i in user:
        if int(i)%2==0:
            o.append(i)
        else:
            o1.append(i)
    print(' '.join(sorted(o)))
    print(' '.join(sorted(o1)))
seperation(input())
