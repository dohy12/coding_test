# https://programmers.co.kr/learn/courses/30/lessons/43164
# 프로그래머스 코팅테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 여행경로
# 풀긴 풀었는데 너무 느리다

from collections import deque

def solution(tickets):
    h = {}
    r_h = {}
    
    tickets.sort()
    
    r_idx = 0
    queue = deque([(r_idx,"ICN")])
    r_h = {r_idx:[["ICN"],[]]} # 루트, used ticket리스트
    while queue:
        q = queue.popleft()
        p_idx, p_w = q

        for t_idx,t in enumerate(tickets):
            if t_idx not in r_h[p_idx][1] and t[0] == p_w:
                r_idx +=1
                queue.append((r_idx,t[1]))
                tmp_route_l,tmp_used_l = list(r_h[p_idx][0]), list(r_h[p_idx][1])
                tmp_route_l.append(t[1])
                tmp_used_l.append(t_idx)
                r_h[r_idx] = [tmp_route_l, tmp_used_l]

                if len(tmp_route_l)==(len(tickets)+1):
                    return tmp_route_l
        
    return []


tickets =[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))