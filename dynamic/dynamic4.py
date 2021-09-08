# https://programmers.co.kr/learn/courses/30/lessons/42897
# 프로그래머스 코팅테스트 연습 > 동적계획법(Dynamic Programming) > 도둑질

h = {}
ml = []
def mon(m,b):
    global h,ml
    if m<0:
        return 0
    maxM = h.get((m,b),-1)
    
    if maxM == -1:
        maxM = max(mon(m-2,b), mon(m-3,b)) + ml[m]
        h[(m,b)] = maxM

    return maxM

def solution(money):
    global h,ml
    ml = money

    h[(0,1)] = money[0]
    h[(1,1)] = 0

    h[(0,0)] = 0

    n = len(money)   

    answer = max(mon(n-1,0), mon(n-2,1),mon(n-2,0),mon(n-3,1))
    print(h)
    return answer


money = [90,0,0,95,1,1]
print(solution(money))



