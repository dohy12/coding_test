# https://programmers.co.kr/learn/courses/30/lessons/82612
# 프로그래머스 코팅테스트 연습 > 위클리 챌린지 > 1주차

def solution(price, money, count):
    cost = int(count*(count+1)/2*price)

    if money > cost:
        return 0
    else :
        return cost - money

price = 3
money = 20
count = 4


print(solution(price, money, count))