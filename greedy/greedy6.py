# https://programmers.co.kr/learn/courses/30/lessons/42862
# 프로그래머스 코팅테스트 연습 > 탐욕법(Greedy) > 구명보트
# 시간초과 
# 시간초과 해결 (pop을 쓰면 시간 초과 걸림)

def solution(people, limit):
    l = sorted(people,reverse=True)
    boat = 0
    n = len(l)
    f = 0
    b = n-1
    while True:
        boat+=1
        if(n>1 and (l[f]+l[b])<=limit):      
            n-=1      
            b-=1
        n-=1
        f+=1         

    answer = boat
    return answer

people = [70, 50, 10, 50]
limit = 100
print(solution(people, limit))