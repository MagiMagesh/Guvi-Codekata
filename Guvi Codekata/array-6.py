def aircapsule(n, user):
    if n == len(user):
        s = 0
        for i in user:
            s = s + int(i)
        if s % n == 0:
            print('0')
        elif s % n != 0:
            print((s % n) + 1)
aircapsule(int(input()), input().split(' '))