list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

added = []

for i in list1:
    for j in list2:
        added.append(i + j)
print(added)