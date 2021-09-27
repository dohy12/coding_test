# 엡실론 공부
# e**x = 1 + x + (x**2)/2 + (x**3)/3! + (x**4)/4! + ... + x**n/n!

def getEs(n): # n : significant
    es = (0.5 * 10**(2-n))
    return es

def getApprox(idx, num):
    tmp = 0
    for i in range(idx+1):
        tmp += num**i/math.factorial(i)
    return tmp

import math

num = 3
es = getEs(5)
ea = 100

curr_approximation = 1 # 현재 추정치
previous_approximation = 1 # 과거 추정치

idx = 0

while es<ea:
    idx +=1
    curr_approximation = getApprox(idx, num)
    previous_approximation = getApprox(idx-1, num)

    ea = (curr_approximation - previous_approximation) / curr_approximation * 100

print(curr_approximation)

print(math.exp(3))