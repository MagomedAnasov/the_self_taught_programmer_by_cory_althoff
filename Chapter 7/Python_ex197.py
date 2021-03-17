shows = ['Breaking the bad',
         'X Files',
         'Fargo']

i = 0

for show in shows:
    new = shows[i]
    shows[i] = new.upper()
    i += 1
print(shows)