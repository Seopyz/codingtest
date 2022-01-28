number, k = map(int, input().split())
result = 0
while True:
    target = (number//k)*k
    result += (number - target)
    number = target
    if number < k:
        break
    result += 1
    number //= k