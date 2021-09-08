# https://programmers.co.kr/learn/courses/30/lessons/42897
# 프로그래머스 코팅테스트 연습 > 동적계획법(Dynamic Programming) > 도둑질
# cgiosy, 강민구님 풀이 (예술이네 ㅋㅋㅋ)

def solution(a):
    x1, y1, z1 = a[0], a[1], a[0]+a[2]
    x2, y2, z2 = 0, a[1], a[2]
    for i in a[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1)+i
        x2, y2, z2 = y2, z2, max(x2, y2)+i

    return max(x1, y1, y2, z2)

money = [10,0,0,1000,10,2]
print(solution(money))

