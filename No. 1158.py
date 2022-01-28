n, k = map(int,(input().split()))
l = [x for x in range(1,n+1)]
idx = 0
ans = []
for i in range(n):
    idx += k-1
    if idx >= len(l):
        idx = idx % len(l)
    ans.append(str(l.pop(idx))) 
print("<",", ".join(ans), ">", sep = "" )