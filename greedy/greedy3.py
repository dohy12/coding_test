# https://programmers.co.kr/learn/courses/30/lessons/42861
# 프로그래머스 코팅테스트 연습 > 탐욕법(Greedy) > 섬연결하기

def solution(n, costs):
    __inf = 999999999

    linked = [0]
    unlinked = list(range(1,n))
    d = {} 

    for cost in costs:        
        d[(cost[0],cost[1])] = cost[2]
        d[(cost[1],cost[0])] = cost[2]

    answer = 0
    while len(unlinked) > 0:
        min_l = __inf
        min_idx = -1
        for i in linked:
            for j in unlinked:
                if(d.get((i,j), __inf )< min_l):
                    min_idx = j
                    min_l = d.get((i,j))
        
        linked.append(min_idx)
        unlinked.remove(min_idx)
        answer += min_l
    return answer


n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n, costs))
