# https://programmers.co.kr/learn/courses/30/lessons/42586
# 프로그래머스 코딩테스트 연습 > 스택/큐 > 기능개발

import math

def solution(progresses, speeds):
    rs = []
    l = [math.ceil((100-progresses[0])/speeds[0])]
    for p,s in zip(progresses[1:],speeds[1:]):
        d = math.ceil((100-p)/s)
        if d>l[0]:
            rs.append(len(l))
            l = [d]
        else :
            l.append(d)
    rs.append(len(l))
    return rs

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))