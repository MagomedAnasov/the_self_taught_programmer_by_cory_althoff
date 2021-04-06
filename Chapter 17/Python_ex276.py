import re
l = "Beautiful is better that ugly."

matches = re.findall("beautiful",l, re.IGNORECASE)

print(matches)