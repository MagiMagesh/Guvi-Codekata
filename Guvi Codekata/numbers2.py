from_user = float(input(''))
sq = (from_user) ** (1 / 2)
if from_user % sq == 0:
    print('Unsaturated')
else:

    print('Saturated')