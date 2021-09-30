# https://programmers.co.kr/learn/courses/30/lessons/86491
# 코딩테스트 연습 > 위클리 챌린지 > 8주차

def solution(sizes):
    w_max = h_max = 0

    for size in sizes:
        w,h = max(size), min(size)
        w_max = max(w_max,w)
        h_max = max(h_max,h)

    return w_max * h_max


def solution2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))