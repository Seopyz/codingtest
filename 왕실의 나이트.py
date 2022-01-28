# position = list(input())
# alpha = {"a" : 1, "b" : 2, "c" : 3, "d": 4, "e" : 5, "f" : "6", "g" : "7", "h" : 8}
# dx = [-2, -2, 2, 2, -1, 1, -1, 1]
# dy = [-1, 1, -1, 1, -2, -2, 2, 2]
# cnt = 0
# x, y = alpha[position[0]], int(position[1])

# if x + dx[0] >=1 and y + dy[0] >= 1:
#     cnt+=1
# if x + dx[1] >=1 and y + dy[1] <= 8:
#     cnt+=1
# if x + dx[2] <= 8 and y + dy[2] >= 1:
#     cnt+=1
# if x + dx[3] <=8 and y + dy[3] <=8:
#     cnt+=1
# if x + dx[4] >=1 and y + dy[4] >=1:
#     cnt+=1
# if x + dx[5] <=8 and y + dy[5] >=1:
#     cnt+=1
# if x + dx[6] >=1 and y + dy[6] <=8:
#     cnt+=1
# if x + dx[7] <=8 and  y + dx[7] <=8:
#     cnt+=1
# print(cnt)

input_data = input()
row = int(input_data[1])
columns = int(ord(input_data[0])) - int(ord("a"))+1
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
cnt=0
for step in steps:
    next_row = row + step[0]
    next_column = columns + step[1]
    if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
        cnt+=1
print(cnt)

    