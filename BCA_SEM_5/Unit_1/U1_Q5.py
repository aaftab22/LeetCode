# find out and display the common and the non common elements in the list using membership operators
list1 = [1, 2, 3, 4]
list2 = [4, 8, 5, 6, 2, 3]

common = []
uncommon = []

for i in list1:
    if i in list2:
        common.append(i)
    else:
        uncommon.append(i)

for j in list2:
    if j not in list1:
        uncommon.append(j)

print("Common Eelement = " , common)
print("Uncommon Eelement = " , uncommon)