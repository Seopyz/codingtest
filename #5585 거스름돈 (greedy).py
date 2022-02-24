#5585 거스름돈 (greedy)
price = int(input())
coins = [500, 100, 50, 10, 5, 1]
change = 1000 - price
cnt = 0
for coin in coins:
    if change > coin:
        cnt += change // coin
        change = change % coin
print(cnt)

a = 1000 - int(input())
b = [500, 100, 50, 10, 5, 1]
count = 0
for i in b:
    count += a // i
    a %= i
print(count)
