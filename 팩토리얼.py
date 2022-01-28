# n = 5
# def fac(n):
#     result = 1
#     for i in range(1,n+1):
#         result*=i
#     print(result)
# fac(n)
def facto(n):
    if n <= 1:
        return 1
    return n * facto(n-1) 
facto(4)