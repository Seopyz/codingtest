#1439 뒤집기 (greedy)
string = input()
stack = []
for i in string:
    if i == "0":
        if stack and stack[-1] == "0":
            continue
        else:
            stack.append("0")
    else:
        if stack and stack[-1] == "1":
            continue
        else:
            stack.append("1")

print(stack.count("1")) if stack.count("0") > stack.count("1") else print(stack.count("0"))

#2
change = 0
prev = '?'
string = input()
for i in string:
    if i != prev: change += 1
    prev = i
print(change//2)

s = input()
count = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1