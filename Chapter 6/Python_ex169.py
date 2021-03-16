n1 = input('Please, enter a noun: ')
v = input('Please, enter a verb: ')
adj = input ('Please, enter adjective: ')
n2 = input ('Please, enter a noun: ' )

r = """ As usual, {} {} {} {}
    """.format(n1,
               v,
               adj,
               n2)
print(r)