def constants(x):
    v = ['a','e','i','o','u']
    o=[]
    for i in x:
        for vowels in i:
            if vowels not in v:
                o.append(vowels)
    print(''.join(o))
constants(input('').lower())