#- 와 - 사이를 괄호친다 50 + 50 - (50+20) - (40+20)
string = input().split("-") # ["50"+"50", "50+20", "40+20"]
num = []
for i in string: #"50+50"
    cnt = 0
    s = i.split("+")  # ["50", "50"]
    for j in s:  # ["50"]
        cnt += int(j)  # cnt에 다더한다
    num.append(cnt)  # num에 합을 넣는다.
n = num[0]
for i in range(1, len(num)):
    n = n - num[i]
print(n)


e = [sum(map(int, input().split("+"))) for i in input().split("-")]
print(e[0]-sum(e[1:]))
