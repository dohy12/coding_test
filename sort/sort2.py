# https://programmers.co.kr/learn/courses/30/lessons/42747
# 프로그래머스 코팅테스트 연습 > 정렬(sort)) > H-Index

import math

def solution(citations):
    c = sorted(citations)

    n = len(c)   
    answer=0
    for h in range(1,n+1):
        if (c[n-h]>=h) and (n-h)<=h:
            answer = h

    return answer

citations = [3,0,6,1,5]
print(solution(citations))