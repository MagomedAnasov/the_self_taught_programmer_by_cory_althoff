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
    board = [' '] * len(word)
    win = False
    print('Welcome to execution!')