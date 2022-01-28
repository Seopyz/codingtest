# n = int(input()) # 도시의 개수 #n
# distance = [map(int, input().split())] #n -1
# cost = [map(int, input().split())] #n
# print(n)
# print(distance)
# print(cost)
# # 가장 최소비용으로 맨 왼쪽 도시에서 오른쪽 도시로 이동하라.
# # 가장 비용이 낮은 도시로 어떻게 도달하냐의 문제
# # 뒤에 도시보다 자신의 도시의 기름값이 낮으면 그냥 쭉 간다.
# idx = 0
# cnt = 0
# while idx < n-1: 
#     for i in range(idx+1,n): #1,4 
#         if cost[idx] > cost[i]:
#             cnt+=sum(distance[idx:i])*cost[idx]
#             idx = i
#             break
# print(cnt)

n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

m = cost[0]
res = 0
for i in range(n-1):
    if cost[i] < m:
        m = cost[i]
    res += m * distance[i]
    
print(res)
