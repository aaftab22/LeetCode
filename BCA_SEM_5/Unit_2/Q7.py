# Write a python program that removes any repeated items from a list so
# that each item appears at most once. For
# instance, the list [1,1,2,3,4,3,0,0] would become  [1,2,3,4,0]
lst1 = [1,1,2,3,4,3,0,0]
result = []
for i in lst1:
    if i not in result:
        result.append(i)

print(result)