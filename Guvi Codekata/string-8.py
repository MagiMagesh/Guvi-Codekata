def lar_num(user):
    user1 = [user.strip('.') for user in user.split(' ')]
    j = 0
    for i in user1:
        try:
            if int(i) > j:
                j = int(i)
        except:
            None
    print(j)
lar_num(input(' '))