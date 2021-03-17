numbers = [3,45,78,23,67,56,89]

while True:
    answer = input('Please guess a number or enter X for exit: ')
    if answer == 'X':
        break
    try:
        answer = int(answer)
    except ValueError:
        print(' Please, enter a number to guess or X for exit: ')
    if answer in numbers:
        print('You are right!')
    else:
        print('You are not right')