# https://programmers.co.kr/learn/courses/30/lessons/42626
# 프로그래머스 코팅테스트 연습 > 힙(Heap) > 더 맵게

import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        elif len(scoville)==0:
            answer = -1
            break
        
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + min2*2
        heapq.heappush(scoville, new_scoville)
        answer+=1

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville,K))