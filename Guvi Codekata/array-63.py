def remvov(string):                 #STRING = codekata
    d = ['a','e','i','o','u']
    a =[]
    for k in string:
            a.append(k)             #a = ['c','o','d','e','k','a','t','a']
    for i in d:
        for j in a:                 # it will work like is (c==a,o==a,d==a,e==a,k==a,a==a,t==a,a==a) & ()
            if i ==j:
                a.remove(i)
    a.reverse()
    if len(a) == len(string) or len(a)==0:
        print(-1)
    else:
        print(''.join(a))
remvov(input())