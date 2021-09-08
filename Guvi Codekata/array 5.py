numlit = int(input())
user = input('').split(' ')
try:
    if len(user)==numlit:
        j=0
        for i in user:
            num = int(i)
            if num > j:
                j = int(i)
                big = j
        for v in user:
            num1 = int(v)
            if num1 < j:
                j = num1
                small = j
        big_inded=(user.index(str(big)))
        small_inded=(user.index(str(small)))
        print(int(big_inded)-int(small_inded))
except:
    None

