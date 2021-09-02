# https://programmers.co.kr/learn/courses/30/lessons/42861
# 프로그래머스 코팅테스트 연습 > 탐욕법(Greedy) > 섬연결하기
# [이시윤]님의 풀이 공부

def ancestor(node, parents):
    if parents[node] == node:
        return node
    else:
        return ancestor(parents[node], parents)

def solution(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    print(edges)
    parents = [i for i in range(n)]

    bridges = 0
    for w, f, t in edges:
        if ancestor(f, parents) != ancestor(t, parents):
            answer += w
            parents[ancestor(f, parents)] = t
            bridges += 1
        if bridges == n - 1:
            break
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n, costs))


# 1. 길이에 따라 edges를 sort한다
# 2. 각 요소들을 parent에 넣는다
# 3. ancestor(node, parents)?
#    3.1) 