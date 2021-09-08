user = input().split(' ')
o=[]
for i in user:
    u = user.index(i)
    if u%2==0:
        o.append(user[u])
s = sorted(o)
for i in s:
    user.remove(i)
print(s)
a=0
b=0
#while b < len(s)+1:
user.insert(a,s[b])
a = a+2
b = b+1
a=2
b=1
#while b < len(s)+1:
user.insert(a,s[b])


a=4
b=2
#while b < len(s)+1:
user.insert(a,s[b])
print(user)



# Actual answer for the question is below mentioned
len_from_user = int(input())
user = input().split(' ')
try:
    if len(user) == len_from_user:
        o=[]
        for i in user:
            u = user.index(i)
            if u%2==0:
                o.append(user[u])
        s = sorted(o)
        for i in s:
            user.remove(i)
        a = 0
        for j in s:
            user.insert(a,j)
            a = a+2
        print(' '.join(user))
except:
    None