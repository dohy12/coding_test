# https://programmers.co.kr/learn/courses/30/lessons/42862
# 프로그래머스 코팅테스트 연습 > 탐욕법(Greedy) > 큰 수 만들기
# 강의 설명대로 구현해보기 (stack 사용 O(n))

def solution(number, k):
    s = [number[0]]
    for i in range(1,len(number)):        
        while k>0:        
            if(len(s)>0): 
                if(number[i]<=s[len(s)-1]):
                    break
                else:
                    k-=1
                    s.pop()
            else:
                break
            
        s.append(number[i])

    s = s[:len(s)-k]
    return ''.join(s)   


number = "99999"
k = 4
print(solution(number, k))