import numpy as np
def arr(b):
   # b = sorted(input('').split(' '))
    a = []
    for i in b:
        a.append(int(i))
    print(a)
    c = np.array((a))
    c.shape = (3,3)
    return c
ard = arr(sorted(input('').split(' ')))
print(ard)