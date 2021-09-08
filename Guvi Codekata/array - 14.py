def occurance(l1,n,l2,t):
    try:
        if l1 == len(n) and l2 == len(t):
            c = dict()
            o =[]
            count = 1
            for i in n:
                if i not in c:
                    c[i] = count
                else:
                    c[i] = count +c[i]
            for i in t:
                if (i) in c.keys():
                    o.append(str(c[i]))
                elif (i) not in c.keys():
                    o.append('Not Present')
            print(' '.join(o))
    except:
        None
occurance(int(input()),input().split(' '),int(input()),input().split(' '))