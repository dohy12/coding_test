# https://programmers.co.kr/learn/courses/30/lessons/43163
# 프로그래머스 코팅테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 단어 변환
# '김다함' 님 풀이 

from collections import deque # 큐를 사용하려면 필요함

def get_adjacent(current, words):
    for word in words:
        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1: # 한 문자만 다를 경우!
            yield word

def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist: # ★ not in ★ 
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]	
print(solution(begin, target, words))