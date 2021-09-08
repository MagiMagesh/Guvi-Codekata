def asci_num(user):
    s=0
    for i in user:
        a =(ord(str(i)))
        s = int(a)+s
    if int(s)%8==0:
        print('1')
    else:
        print('0')


asci_num(input())