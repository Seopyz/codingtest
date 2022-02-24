array = [4,5,1,3,5,9,8,4,5,2,1,3,6,5,4,7,8,5,3,1,5,6,7,9,5,4,6,2,1,3,5,4]
cnt = [0] * (max(array)+1)
for i in range(len(array)):
    cnt[array[i]] += 1

for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i, end = " ")