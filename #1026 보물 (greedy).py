#1026 보물 (greedy)
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(a)
b = sorted(b, reverse=True)
answer = 0
for i in range(len(a)):
    answer += a[i] * b[i]

print(answer)