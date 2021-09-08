user = int(input())
u = []
while user > 0:
    a = user % 10
    u.append(int(a))
    user = user // 10
s= (sum(u))
a=1
for i in u:
    a = a*i
v = s+a
print(v)

if user == int(v) or v ==user:
    print('g')