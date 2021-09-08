tic_input = int(input())
val = input()
date = int(input())

tic_num = val.split(' ')
output =[]
for i in tic_num:
    if int(i)%date ==0:
        a = 1
        output.append(str(a))
    else:
        b = 0
        output.append(str(b))
print(' '.join(output))