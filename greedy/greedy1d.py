# https://programmers.co.kr/learn/courses/30/lessons/42862
# 프로그래머스 코팅테스트 연습 > 탐욕법(Greedy) > 체육복
# 강의 내용2

def solution(n, lost, reserve):
    s = set(lost) & set(reserve)    # 체육복 가져왔고 도난도 당함
    l = set(lost) - s               # 체육복 도난당함
    r = set(reserve) - s            # 체육복 남는 놈들

    for x in sorted(r):     # 체육복 남는 놈들 sort해서 확인
        if x - 1 in l:      # 먼저 앞선놈이 없으면 앞놈 빌려줌
            l.remove(x-1)
        elif x + 1 in l:    # 그후 뒷놈 없으면 뒷놈 빌려줌
            l.remove(x+1)

    return n - len(l)
    
