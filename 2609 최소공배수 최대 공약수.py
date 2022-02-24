a,b = map(int, input().split())
def GCD(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a,b):
    return a * b // GCD(a,b)

import math
a,b = map(int, input().split())
print(math.gcd(a,b))
print(math.lcm(a,b))