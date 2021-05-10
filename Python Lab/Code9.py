while True:
    x = input('Enter your marks : ')
    x = int(x)

    if x >= 80:
        print('A+')
    elif x >= 75 and x < 80:
        print('A')
    elif x >= 70 and x < 75:
        print('A-')
    elif x >= 65 and x < 70:
        print('B+')
    else:
        print('You should be more attentive')
        
