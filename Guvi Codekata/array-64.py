def position(n, array1, n1, array2):             # a1= 95 68 62 58 55 41 30    a2= 45 61
    if n == len(array1) and n1 == len(array2):
        out = []
        a1 = []
        a2 =[]
        for i in array1:
            a1.append(int(i))                   # a1 = [95. 68. 62. 58. 55. 41. 30]
        for ji in array2:
            a1.append(int(ji))                  #a1 = [95. 68. 62. 58. 55. 41. 30, 45,61]
            a2.append(int(ji))                  #a2 = [45, 61]
            b = sorted(a1)  # a1 = [1,2,5,6,8,9]    #a1 = [30,41,45,55,58,61,62,68,95]
            b.reverse()  # a1 = [9,8,6,5,2,1]       #a1 = [95,68,62,61,58,55,45,41,30]
            la2 = 1                       #a2 = 2
            n =0
            try:
                while la2 ==1:
                    first = a2[n]                   #if n = 0 first = a2[0]=45
                    ist_index = b.index(first)
                    out.append(ist_index+1)
                    n = n+1
            except:
                None
        output = []
        for i in out:
            output.append(str(i))
        print(' '.join(output))
position(int(input()), input().split(' '), int(input()), input().split(' '))
