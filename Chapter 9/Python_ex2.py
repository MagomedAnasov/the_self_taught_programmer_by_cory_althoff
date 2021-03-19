answer = input('Please, enter some words: ')

with open('answer.csv', 'w') as f:
    f.write(answer)
