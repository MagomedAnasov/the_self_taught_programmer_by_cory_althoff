questions = ['What is your name?: ',
             'What is your favorite color?: ',
             'What are you doing?: ']
n = 0

while True:
    print('Enter X for exit!')
    a = input(questions[n])
    if a == 'X':
        break
    n = (n + 1) % 3