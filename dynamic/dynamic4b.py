# https://programmers.co.kr/learn/courses/30/lessons/42897
# 프로그래머스 코팅테스트 연습 > 동적계획법(Dynamic Programming) > 도둑질
# 시간초과 -> hash를 list로 바꾸어 해결

def solution(money):    
    n = len(money)   
    l = [[0,0] for i in range(n+2)]

    l[2][1] = money[0]
    for i in range(3,n+2):
        maxM = max(l[i-2][0],l[i-3][0])
        l[i][0] = maxM + money[i-2]

    for i in range(3,n+1):
        maxM = max(l[i-2][1],l[i-3][1])
        l[i][1] = maxM + money[i-2]

    print(l)
    answer = max(l[n+1][0], l[n][0], l[n][1], l[n-1][1])
    return answer

money = [10,0,0,1000,10,2]
print(solution(money))


