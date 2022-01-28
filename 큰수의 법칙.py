# n, m, k = map(int, input().split())
# l = list(map(int, input().split()))
# l.sort()
# first = l[n-1]
# second = l[n-2]
# result = 0
# cnt = 0
# for i in range(m):
#     if cnt <k:
#         result+=first
#         cnt+=1
#     else:
#         result+=second
#         cnt = 0
# print(result)


n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]
cnt = int(m / (k + 1 ))*k
cnt += m % (k+1)



    
