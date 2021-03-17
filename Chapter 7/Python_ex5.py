list1 = [8, 3, 5, 7]
list2 = [9, 3, 1, 6]

added = []

for i in list1:
    for j in list2:
        added.append(i * j)
print(added)