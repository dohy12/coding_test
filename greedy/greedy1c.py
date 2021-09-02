# https://programmers.co.kr/learn/courses/30/lessons/42862
# 프로그래머스 코팅테스트 연습 > 탐욕법(Greedy) > 체육복
# 강의 내용

def solution(n, lost, reserve):
    answer=0

    u = [1] * (n+1) # index를 여분으로 줘서 귀찮게 앞뒤 애들 신경 안써줘도 된다!
    for i in reserve:
        u[i] += 1

    for i in lost:
        u[i] -= 1

    for i in range(1, n +1):
        if u[i-1] == 0 and u[i] == 2:
            u[i - 1:i + 1] = [1,1]
        elif u[i] == 2 and u[i+1] == 0:
            u[i:i + 2] = [1,1]
        
    return len([x for x in u[1:-1] if x>0]) # 앞뒤에서 1씩 뺀 u에서 x가 0보다 큰 u를 가져온다.


n = 10
lost = [1, 5, 8, 3, 7]
reserve = [7, 5, 2, 9, 6]

print(solution(n, lost, reserve))