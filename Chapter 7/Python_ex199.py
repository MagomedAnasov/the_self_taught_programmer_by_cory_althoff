# List of shows
shows = ['Breaking the bad',
         'X Files',
         'Fargo']
# List of coms
coms = ('Big Bang Theory',
        'Friends',
        'Fathers daughters')
# Empty list for all shows
all_shows = []

# For loop for adding shows to list of all shows
for show in shows:
    show = show.upper()
    all_shows.append(show)

# For loop for adding coms to list of all shows
for com in coms:
    com = com.upper()
    all_shows.append(com)

print(all_shows)