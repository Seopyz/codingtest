n = int(input())
a = list(map(int, input().split()))
a.sort()
sum = 0
temp = 0
for i in range(n):
    temp += a[i]
    sum += temp

print(sum)

