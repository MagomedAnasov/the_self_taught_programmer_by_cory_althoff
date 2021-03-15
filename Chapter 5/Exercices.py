# 1 - List of my favorite bands

bands = ['U2', 'Led Zeppelin', 'Chemical Brothers']
print(bands)


# 2 - List of tuples with coordinates

tuple1 = ('54.323232', '23.56567565')
tuple2 = ('52.323232', '13.56567565')

list = [tuple1,tuple2]

print(list)

# 3 - Create a dictionary with personal data

my_dict = {'Age': '33',
           'Height': '178',
           'Weight': '79'}

print(my_dict)

# 4 - Program that ask user about weight, color or actor



answer = input('Please enter your weight: ')

if answer in my_dict:
    result = my_dict[answer]
    print(result)

# 5 - Dictionary with my favorite bands and lists of their songs

bands = {'U2': ['Magnificent',
                'One',
                'Mofo'],
         'Chemical Brothers': ['Hey boy hey girl',
                               'Believe']
}

print(bands)