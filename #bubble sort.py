#bubble sort
l = [10, 1, 6, 8, 3, 2, 9, 7, 5, 4]
for i in range(len(l)):
    for j in range(0,9-i,):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]

print(l)