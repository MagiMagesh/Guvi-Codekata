from_user = input('')
split_user = from_user.split(' ')
common_a_b = []
common_a_b_c = []
a = split_user[0]
b = split_user[1]
c = split_user[2]
for a1 in a:
    if a1 in b:
        common_a_b.append(a1)
for b1 in common_a_b:
    if b1 in c:
        common_a_b_c.append(b1)
print(common_a_b_c)
print(" ".join(common_a_b_c))