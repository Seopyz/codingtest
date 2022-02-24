n,k = map(int, input().split())
l = [i for i in range(1,n+1)]
idx = 0
answer = []
for i in range(n):
    idx += k-1
    if idx >= len(l):
        idx = idx % len(l)
    answer.append(str(l.pop(idx)))