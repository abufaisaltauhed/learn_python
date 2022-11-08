def bubble_sort(l1):
    for len_x in range(len(l1)-1,0,-1):
        for i in range(len_x):
            if l1[i] > l1[i+1]:
                tmp = l1[i]
                l1[i] = l1[i+1]
                l1[i+1] = tmp

l1 = [19,2,31,45,6,11,121,27]
bubble_sort(l1)
print(l1)

