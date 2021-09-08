p = input('')
q= p.split(' ')
a =q[0]
b =q[1]
factors_of_a =[]
factors_of_b=[]

for i in range(1,(int(a)+1)):
    if int(a)%i==0:
        factors_of_a.append(i)
print(factors_of_a)

for n in range(1,(int(b)+1)):
    if int(b)%n==0:
        factors_of_b.append(n)
print(factors_of_b)
common = []
for value in factors_of_a:
    if value in factors_of_b:
        common.append(value)
if len(common)==1:
    print('1')
else:
    print('o')
print(common)