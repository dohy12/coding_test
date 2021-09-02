# https://programmers.co.kr/learn/courses/30/lessons/42861
# 프로그래머스 코팅테스트 연습 > 탐욕법(Greedy) > 단속카메라
# [장현우]님의 풀이

def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30001

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer