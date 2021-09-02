# https://programmers.co.kr/learn/courses/30/lessons/42861
# 프로그래머스 코팅테스트 연습 > 탐욕법(Greedy) > 단속카메라

def solution(routes):
    answer = 0

    routes = sorted(routes)    
    idx_start = 0
    while 1:    
        if idx_start == len(routes):
            break        

        answer += 1
        max_x = routes[idx_start][1]
        idx_start +=1
        
        for idx in range(idx_start, len(routes)):
            if(routes[idx][0]<=max_x):
                max_x = min(routes[idx][1],max_x)
                idx_start+=1
            else:
                break
    
    return answer

routes = [[-20,15], [-20,15], [-20,15], [-20,15], [-20,15]]

print(solution(routes))