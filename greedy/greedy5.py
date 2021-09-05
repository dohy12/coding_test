# https://programmers.co.kr/learn/courses/30/lessons/42862
# 프로그래머스 코팅테스트 연습 > 탐욕법(Greedy) > 큰 수 만들기

def solution(number, k):
    i=0
    for j in range(k):
        while True:
            n = len(number)
            if(i==(n-1)):
                number = number[:n-1]
                i= max(0,i-1)
                break
            else:
                t2 = number[i+1]
            t1 = number[i]        
            
            if(t1<t2):
                number = number[:i] + number[i+1:n]
                i= max(0,i-1)
                break
            i+=1        
    
    answer = ''.join(number)
    return answer

number = "999999999"
k = 4
print(solution(number, k))