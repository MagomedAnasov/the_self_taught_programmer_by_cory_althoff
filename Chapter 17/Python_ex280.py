import re

t = "__one__ __two__ __three___"

# In Python ? sign in regex means that it will stop once there is exact match. Without ? sign it would find all matches
found = re.findall("__.*?__", t )
for match in found:
    print(match)