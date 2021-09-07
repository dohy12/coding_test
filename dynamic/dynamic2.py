# https://programmers.co.kr/learn/courses/30/lessons/43105
# 프로그래머스 코팅테스트 연습 > 동적계획법(Dynamic Programming) > 정수 삼각형

h = {}
tri = []
def route(floor, n):
    global h, tri
    maxR = h.get((floor, n),-1) 
    if maxR == -1:
        l = []
        left = right = (-1,-1)
        left  = (floor-1, n-1)
        right = (floor-1, n)

        if (left[0]!=-1):
            if(left[1]>=0):
                l.append(route(left[0],left[1]))
            if(right[1]<floor):
                l.append(route(right[0],right[1]))

            maxR = max(l) + tri[floor][n]
            h[(floor,n)] = maxR
            
    return maxR

def solution(triangle):
    global tri, h
    tri = triangle
    h[(0,0)] = tri[0][0]

    l = []
    n = len(triangle)
    for i in range(n):        
        l.append(route(n-1,i))
        
    answer = max(l)
    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
