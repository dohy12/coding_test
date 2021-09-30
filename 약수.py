import math

def gcd(n):
    tmp = []
    for idx in range(1,int(math.sqrt(n))+1):
        if (n%idx == 0):
            tmp.append(idx)

    return tmp

n = 3486
print(n, gcd(n))

n = 101
print(n, gcd(n))


print((9**101)%10, (4**9)%13)