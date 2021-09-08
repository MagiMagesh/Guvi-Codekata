input_len = 6
input_str = input('')
values = input_str.split(' ')
print(values)
n=0
sum=0
empty = []
for i in values:
    if values[n] < values[n+1]:
        sum = sum +int(i)
        n = n + 1

print(sum)