def found(sentence,string):
    s = string[0]
    o = dict()
    count = 1
    n = 0
    for i in sentence:
        if i not in o:
            o[i] = count
        else:
            o[i] = count + o[i]
    if s in sentence:
        print(o[s])
    else:
        print(-1)

found(input().split(' '),input().split(' '))