shows = ['Breaking the bad',
         'X Files',
         'Fargo']
for i, show in enumerate(shows):
    new = shows[i]
    new = new.upper()
    shows[i] = new
print(shows)

colors = ['red', 'green', 'blue']
for num, color in enumerate(colors):
    print(str(num) + '-й цвет: ' + color)
