def mid(arr):
    array=[]
    for i in arr:
        array.append(i)
    m = len(array)//2
    if len(array)%2!=0:
        array[m]='*'
    elif len(array)%2==0:
        array[m]='*'
        array[m-1]='*'
    print(''.join(array))
mid(input(''))