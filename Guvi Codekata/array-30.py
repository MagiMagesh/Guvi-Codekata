def mid(array):
    m = len(array)//2
    if len(array)%2!=0:
        array.replace(array[m],'*')
    elif len(array)%2==0:
        array.replace(array[m],'*')
        array.replace(array[m-1],'*')
    print(array)
mid(str(input()))