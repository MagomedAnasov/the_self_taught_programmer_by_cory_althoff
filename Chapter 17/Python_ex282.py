import re
line = "I like $"

m = re.findall('\\$',line, re.IGNORECASE)
print(m)