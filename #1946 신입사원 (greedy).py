#1946 ė ėėŽė (greedy)
case = int(input())
for i in range(case):
    n = int(input())
    max_person = n
    people = []
    for j in range(n):
        people.append(list(map(int, input().split())))
    for k in range(n):
        for l in range(n):
            if people[k][0] < people[j][0] and people[k][1] < people[j][1]:
                max_person -= 1
    print(max_person)