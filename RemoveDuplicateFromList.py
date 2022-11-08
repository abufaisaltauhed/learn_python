

RemoveDuplicateFromList.py
l1 = [21,1,32,1,43,1,54,23,46,78,43]
print("Before Removing the Duplicate ",l1) 
c = []
for i in l1:
    if i not in c:
        c.append(i)
print(c)

