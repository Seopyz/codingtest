
# while True:
#     string = input()
#     ans = [0]*4
#     if not string:
#         break
#     for i in range(len(string)):
#         if ord(string[i]) >=65 and ord(string[i]) <=90:
#             ans[1]+=1
#         elif ord(string[i]) >=97 and ord(string[i]) <=122:
#             ans[0]+=1
#         elif string[i].isdigit():
#             ans[2]+=1
#         else: ans[3]+=1
#     print(ans)

import sys
while True:
    line = sys.stdin.readline().rstrip("\n")
    up, lo, sp, nu = 0, 0, 0, 0
    if not line:
        break
    for i in line:
        if i.isupper():
            up += 1
        elif i.islower():
            lo += 1
        elif i.isdigit():
            nu += 1
        elif i.isspace():
            sp += 1
    sys.stdout.write("{} {} {} {}\n".format(lo, up, nu, sp))