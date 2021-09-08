from_user = str(input(''))
list_from_user = from_user.split()
l = len(list_from_user)-1
while l >=0:
    for i in list_from_user[l]:
        print(i + ' ')
        break
    l = l -1