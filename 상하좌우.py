# n = int(input())
# cmd = list(map(str, input().split()))
# x, y = 1, 1
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ["L", "R", "U", "D"]
# for i in range(len(cmd)):
#     if cmd[i] == move_types[0] and y > 1:
#         x, y = x+dx[0], y+dy[0]
#     elif cmd[i] == move_types[1] and y < n:
#         x, y = x+dx[1], y+dy[1]
#     elif cmd[i] == move_types[2] and x < 1:
#         x, y = x+dx[2], y+dy[2]
#     elif cmd[i] == move_types[3] and x < n:
#         x, y = x+dx[3], y+dy[3]
# print(x,y)

n = int(input())
plans = input().split()
x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny <1 or nx >n or ny >n:
        continue
    x, y = nx, ny

print(x, y)

