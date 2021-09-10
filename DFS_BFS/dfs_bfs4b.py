# https://programmers.co.kr/learn/courses/30/lessons/43164
# 프로그래머스 코팅테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 여행경로
# 강의 내용 듣고 짜본 코드

from collections import deque
import heapq

def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0],[]) + [t[1]]
    
    for r in routes.values():
        r.sort(reverse=True)

    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))