# https://programmers.co.kr/learn/courses/30/lessons/49189
# 코딩테스트 > 그래프 > 가장 먼 노드    

from collections import deque

def solution(n, edge):
    graph = [[] for x in range(n)]

    for e in edge:
        graph[e[0]-1].append(e[1]-1)
        graph[e[1]-1].append(e[0]-1)

    distances = [-1 for x in range(n)]
    distances[0] = 0

    queue = deque([0])

    while queue:
        node = queue.popleft()
        
        for e in graph[node]:
            if distances[e] == -1:
                queue.append(e)
                distances[e] = distances[node] + 1  

    max_distance = max(distances)

    cnt = 0
    for d in distances:
        if d == max_distance:
            cnt+=1 

    return cnt

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))
