#에라토스테네스의 체
n = int(input())
numbers = list(map(int, input().split()))
for i in numbers:
    error = 0
    if i >1:
        for i in range(2, i+1):
            if numbers % i == 0:
                error += 1
    

