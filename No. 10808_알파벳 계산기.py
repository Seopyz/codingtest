# word = input()
# alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# stack = []
# for i in range(len(alphabet)):
#     stack.append(word.count(alphabet[i]))
# print(*stack)

import sys
a = [0 for i in range(26)]
s = sys.stdin.readline().rstrip()
for i in s:a[ord(i) - ord("a")] +=1
for i in a:print(i, end = " ")