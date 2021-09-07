# https://programmers.co.kr/learn/courses/30/lessons/42895
# 프로그래머스 코팅테스트 연습 > 동적계획법(Dynamic Programming) > N으로 표현

import math

ch = -1
h = {}

def calc(cnt, N, number):    
    global ch # 글로벌 변수 쓰려면 가져와야함
    s = set()
    if h.get(cnt, []) == []:
        s.add(int(str(1)*cnt)*N) # int(str(1)*cnt)*N로 대체 가능
        for i in range(cnt-1, math.ceil(cnt/2)-1,-1):
            for j in calc(i, N, number):
                for k in calc(cnt-i, N, number):                
                    s.add(j + k)
                    s.add(j - k)
                    s.add(j * k)
                    if k!=0:
                        s.add(math.floor(j / k))            

        for i in range(math.ceil(cnt/2)-1, 0,-1):
            for j in calc(i, N, number):
                for k in calc(cnt-i, N, number):   
                    s.add(j - k)
                    if k!=0:
                        s.add(math.floor(j / k))

        h[cnt] = s
        for i in s: # 원하는 number가 있는 지 체크
            if i == number:
                ch = cnt
                break
    else :
        s.update(h[cnt])
    
    return s

def solution(N, number):
    global ch
    for i in range(1,9):
        if(ch == -1):
            calc(i,N,number)
        else :
            break

    answer = ch
    return answer

print(solution(5,100))