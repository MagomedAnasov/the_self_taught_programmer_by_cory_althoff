def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Welcome to execution!')

    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Enter a letter: '
        guess = input(msg)
        if guess in rletters:
            ind = rletters.index(guess)
            board[ind] = guess
            rletters[ind] = '$'
        else:
            wrong += 1
        print(''.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('You won! The word was: ')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You lose! The word was {}'.format(word))

list = ['bitch', 'cat', 'horse']

for char in list:
    hangman(char)