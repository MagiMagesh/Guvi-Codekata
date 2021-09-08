def first_neg_int(n, array, k):
    try:
        if n == len(array):
            o = []
            for i in array:
                if int(i) < 0:
                    o.append(i)
            k = o[0]
            if len(o) > 0:
                print(k, ' '.join(o))
            else:
                for i in range(len(array)):
                    print(' '.join('0'))


    except:
        None


first_neg_int(int(input()), input().split(), int(input()))