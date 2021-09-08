from_user = input('')
array_from_user = input('')

v = from_user.split(' ')
n=v[0]
k=v[1]
v_array = array_from_user.split(' ')
if k in v_array:
    print(k)
else:
    print('-1')