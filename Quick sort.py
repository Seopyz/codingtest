#Quick sort
l = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
def quick_sort(data, start, end):
    if start >= end:
        return
    key = start
    i = start + 1
    j = end

    while i <= j:
        while data[i] <= data[key]:
            i+=1
        while data[j] >= data[key] and j > start:
            j-=1

        if i > j:
            data[j], data[key] = data[key], data[j]
        else:
            data[j], data[i] = data[i], data[j]
    quick_sort(data, start, j-1)
    quick_sort(data, j+1, end)

quick_sort(l, 0, 9)
print(l) 
