import math

def exp(n):
    prev_num = 0
    curr_num = 1
    i = 0

    while True:
        if prev_num == curr_num:
            return curr_num
        i += 1
        prev_num = curr_num
        tmp = (n ** i) / math.factorial(i)
        curr_num = curr_num + tmp
        print("idx=",i," curr_num=",curr_num)

n = -10
print("exp(10) = ",exp(n))
print("exactValue = ", math.exp(n))
