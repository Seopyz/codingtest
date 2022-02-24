#10610 30 (greedy)
number = list(map(int, input()))
sum = 0
if 0 not in number:
    print(-1)
else:
    for i in range(len(number)):
        sum += number[i]
    if sum % 3 == 0 and number in 0:
        print(number.sort(reverse = True))