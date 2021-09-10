# https://programmers.co.kr/learn/courses/30/lessons/43162
# 프로그래머스 코팅테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 네트워크

def getParent(i, l):
    if i == l[i]:
        return i
    else :
        return getParent(l[i],l)

def solution(n, computers):
    l = [x for x in range(n)] # 부모 연결

    for l_idx, links in enumerate(computers):
        for idx, link in enumerate(links[l_idx:], start=l_idx):
            if(l_idx != idx and link == 1) :
                l[getParent(idx, l)] = getParent(l_idx, l)

    answer = 0 
    for idx, link in enumerate(l):
        if(idx == link):
            answer+=1
    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n, computers))