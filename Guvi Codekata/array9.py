b = input()
a = b.split(' ')
l = len(a)
print(l)
n=0
output= []
while l>0:
    if int(val[n])<int(val[n+1]):
        min = int(val[n])
        output.append(min)
    else:
        min = int(val[n+1])
        output.append(min)
    n = n+1
    l = l-1
print(output)


#####SOME MODIFIED PROBLEM
b = input()
val = b.split(' ')
l = len(val)
n=0
output= []
while l>1:
    while n <l-1:
        while int(val[n+1])<int(val[n]):
            min = int(val[n + 1])
            output.append(min)
        n = n + 1

    l = l - 1

   # if int(val[n+1])<int(val[n]):
       # min = int(val[n+1])
       # output.append(min)
    #else:
     #   min = int(val[n])
       # output.append(min)
    #n = n+1

 #   l = l-1
print(output)




#recent working 05-06-2021

def nxt_smallest(user):
    user1 = user
    print(user1)
    for i in user:
        for j in user1:
            if j < i:
                print(j)
                pass
nxt_smallest(input().split(' '))




def nxt_smallest(user):
    l = len(user)+2
    n=0
    y = True
    try:
        while l > 0:
            while n < l:
                if int(user[n]) > int(user[n+1]):
                    print(user[n+1])
                n = n+1
            l=l-1
            n = n + 1
    except:
        print(-1)
nxt_smallest(input().split(' '))