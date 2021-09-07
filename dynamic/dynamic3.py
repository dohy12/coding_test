# https://programmers.co.kr/learn/courses/30/lessons/42898
# 프로그래머스 코팅테스트 연습 > 동적계획법(Dynamic Programming) > 등굣길

h = {}
p = []
def route(x, y):
    global h,p
    maxR = h.get((x,y),-1)
    if maxR == -1:
        if x==-1 or y==-1:
            h[(x,y)] = 0
            return 0

        for i in p:
            if x==(i[0]-1) and y==(i[1]-1):
                h[(x,y)] = 0
                return 0
        
        u_pos = (x,y-1) 
        l_pos = (x-1,y)

        maxR = route(u_pos[0],u_pos[1]) + route(l_pos[0],l_pos[1])
        h[(x,y)] = maxR

    return maxR




def solution(m, n, puddles):
    global h,p
    h[(0,0)] = 1
    p = puddles
    
    
    answer = route(m-1, n-1)
    print(h)
    return answer

m = 4
n = 3
puddles = [[2,2]]

print(solution(m, n, puddles))
