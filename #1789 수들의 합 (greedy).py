#1789 수들의 합 (greedy)
number = int(input())
recent_number = 0
while number >= recent_number+1:
    recent_number += 1
    number = number - recent_number

print(recent_number)