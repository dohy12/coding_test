# https://programmers.co.kr/learn/courses/30/lessons/86048
# 프로그래머스 코팅테스트 연습 > 위클리 챌린지 > 7주차



def solution(enter, leave):
    n = len(enter)
    h = {}
    e_cnt = l_cnt = 0

    rs = [0 for x in enter]
    while l_cnt < n:
        if leave[l_cnt] not in h:
            h[enter[e_cnt]] = True    
            sets = set(enter[:e_cnt]) - set(leave[:l_cnt])           
            e_cnt += 1       

            for s in sets:
                rs[s-1] +=1 
            print(e_cnt)
            rs[enter[e_cnt-1]-1] = len(sets)
        else:
            l_cnt +=1
    return rs
    

enter = [1,4,2,3]
leave = [2,1,3,4]

print(solution(enter, leave))