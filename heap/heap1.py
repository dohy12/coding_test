# https://programmers.co.kr/learn/courses/30/lessons/42626
# 프로그래머스 코팅테스트 연습 > 힙(Heap) > 더 맵게

import heapq

def solution(scoville, K):
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)    
    
    answer=0
    while True:
        if heap[0]<K:
            if len(heap)>1:
                answer +=1
                food = heapq.heappop(heap) + heapq.heappop(heap)*2
                heapq.heappush(heap, food)
            else:
                answer = -1
                break
        else:
            break
    
    print(heap)
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7

print(solution(scoville,K))