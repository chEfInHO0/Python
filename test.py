def soma(a,b):
    add = a+b
    return add

loop = True
while loop:
    x = input('Select a number: ')
    y = input('Select a second number: ')

    try:
        print(soma(int(x),int(y)))
    except ValueError:
        print('One of the values isnt a number')
    print('Wanna run it again?')
    answer = input('Y[Yes] / N[No]').strip().upper()
    valid_answer = ('Y','N')
    while answer not in valid_answer:
        print('Invalid action, try again')
        answer = input('Y[Yes] / N[No]').strip().upper()
    if answer == 'Y':
        loop = True
    else:
        loop = False