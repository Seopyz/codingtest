n = int(input())
p = list(map(int, input().split()))
p = sorted(p)
cnt = 0
for i in range(n):
    for j in range(i+1):
        cnt += p[j]
print(cnt)