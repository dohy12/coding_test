# https://programmers.co.kr/learn/courses/30/lessons/42627
# 프로그래머스 코팅테스트 연습 > 힙(Heap) > 디스크 컨트롤러
# 

import heapq
import math

def solution(jobs):
    jobs = sorted(jobs)
    n = len(jobs)
    all_time = 0
    cal_time = 0
    heap = []    
    i =0
    while True:
        if len(heap)==0:
            if(i < n):
                heapq.heappush(heap, (jobs[i][1],jobs[i][0]))
                all_time = jobs[i][0]
                i+=1
            else:
                break

        job = heapq.heappop(heap)    
        all_time += job[0]
        cal_time += all_time - job[1]

        while True:            
            if (i<n):
                if jobs[i][0] <= all_time:
                    heapq.heappush(heap, (jobs[i][1],jobs[i][0]))
                    i+=1
                else:
                    break
            else:
                break

    answer = math.floor(cal_time/n)
    return answer

jobs = [[0, 3], [4, 4], [5, 3], [4, 1]]
print(solution(jobs))

    