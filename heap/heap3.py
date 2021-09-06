# https://programmers.co.kr/learn/courses/30/lessons/42628
# 프로그래머스 코팅테스트 연습 > 힙(Heap) > 이종우선순위큐

import heapq

def solution(operations):
    heapMin = []
    heapMax = []

    idx = 0
    for o in operations:
        os = o.split()
        n = int(os[1])

        if os[0] == 'I':
            heapq.heappush(heapMin,(n,idx))
            heapq.heappush(heapMax,(-n,idx))
            idx+=1
        else :
            if len(heapMin)>0:
                if n == 1:
                    tmp = heapq.heappop(heapMax)
                    heapMin.remove((-tmp[0],tmp[1]))
                else :
                    tmp = heapq.heappop(heapMin)
                    heapMax.remove((-tmp[0],tmp[1]))

    minRs = 0
    maxRs = 0
    if len(heapMin)>0:
        minRs = heapMin[0][0]
        maxRs = -heapMax[0][0]

    answer = [maxRs,minRs]

    return answer

operations = ["I 16","D 1"]
print(solution(operations))