try:
    from_user = input('')
    values  = str(input(''))
    output= []
    big = None
    for i in values:
        if i > values[0]:
            output.appeend(i)
    a = sort(output)
    print(' '.join(output))
except:
    print('-1')