# https://programmers.co.kr/learn/courses/30/lessons/43163
# 프로그래머스 코팅테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 단어 변환
# zip, generator(X), deque 연습용 

from collections import deque

def solution(begin, target, words):
    h = {begin: 0}
    used = [0 for x in words]
    queue = deque([begin])

    while queue:
        ch_w = queue.popleft()
        for idx,w in enumerate(words):            
            cnt = 0
            if used[idx]==0:
                for i,j in zip(ch_w,w):
                    if (i!=j):
                        cnt+=1
                if cnt == 1:
                    queue.append(w)
                    used[idx]=1
                    h[w] = h[ch_w] + 1
                    if w == target:
                        queue = []
                        break
    return h.get(target,0)

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]	
print(solution(begin, target, words))