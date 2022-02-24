#4796 캠핑 (greedy)
i = 1
while True:
    l, p, v = map(int, input().split())
    if l + p + v ==0:
        break

    a = v // p
    b = v %p
    if l < b:
        b = 1
    print("Case %d: %d" %(i, a * l +b))