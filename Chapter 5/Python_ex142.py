facts = dict()

# Add a value
facts['code'] = 'funny'

# Look up a key
print(facts['code'])

# Add a vlaue
facts['Bill'] = 'Gates'
print(facts['Bill'])

# Add a value
facts['foundation'] = '1776'

# Look up a key
print(facts['foundation'])

print('Bill' not in facts)

del facts['code']

print(facts)