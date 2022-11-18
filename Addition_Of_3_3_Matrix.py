#cat Addition_Of_3_3_Matrix.py 
m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[11,12,13],[14,15,16],[17,18,19]]
for a in m1:
    print(a)
print("...............")    
for b in m2:
    print(b)
print("ADD the MATRIX")

#m1 = [[1,2,3]]
#m2 = [[11,12,13]]
l1 = []
l2 = []
for i in range(3):
    x = m1[i]
    y = m2[i]
    l1.append([])
    for j in range(3):
        #print(l1)
        l1[i].append(x[j]+y[j])
print(l1)    


