# 공부용 연습

import functools

def comparator(a,b):
    str1 = a + b
    str2 = b + a

    return (int(str1) > int(str2)) - (int(str1) < int(str2)) #  str1이 더 크면 1 str2가 더 크면 -1 같으면 0

def solution(numbers):
    nums = [str(x) for x in numbers]
    nums.sort(key = functools.cmp_to_key(comparator), reverse=True)

    return str(int(''.join(nums)))


numbers = [1,12,42,10]
print(solution(numbers))