# https://programmers.co.kr/learn/courses/30/lessons/42626
# 프로그래머스 코팅테스트 연습 > 힙(Heap) > 더 맵게

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    answer=0
    while True:
        if scoville[0]<K:
            if len(scoville)>1:
                answer +=1
                food = heapq.heappop(scoville) + heapq.heappop(scoville)*2
                heapq.heappush(scoville, food)
            else:
                answer = -1
                break
        else:
            break
    
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville,K))