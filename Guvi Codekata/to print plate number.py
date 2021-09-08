a = input('')
num = ['0','1','2','3','4','5','6','7','8','9']
d = 0
for i in a:
    if i in num:
        d = int(i)+d
print(d)