# https://programmers.co.kr/learn/courses/30/lessons/42746
# 프로그래머스 코팅테스트 연습 > 정렬(sort)) > 가장 큰수

import math

def solution(numbers):
    l = []
    for ch in numbers:
        tmp =0
        if ch != 0 :
            ch_l = math.floor(math.log10(ch))            
            
            lt = 3 - ch_l
            for_lt = lt
            if lt == 2:
                for_lt =1

            tmp = ch    
            for i in range(for_lt):
                tmp += ch * pow(pow(10,ch_l+1),i+1)

            if lt == 1:
                tmp = math.floor(tmp / 100)    

        l.append((tmp,ch))

    l.sort(reverse = True)
    ch_0 = 0
    answer = ''
    for i in l:
        if(i[1]!=0):
            ch_0+=1
        answer += str(i[1])

    if ch_0==0:
        answer = '0'
    
    return answer

numbers = [0,1,0,0]
print(solution(numbers))