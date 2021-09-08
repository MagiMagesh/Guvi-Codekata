from_user = (input(''))
values  = from_user.split(' ')
a = int(values[0])
b = int(values[1])
factors_a= []
factors_b = []
for i in range(1,(a+1)):
    if a%i==0:
        factors_a.append(i)
#print(factors_a)

for z in range(1,(b+1)):
    if b%z==0:
        factors_b.append(z)
#print(factors_b)
commom= []
for values in factors_b:
    if values in factors_a:
        commom.append(values)
print(max(commom))