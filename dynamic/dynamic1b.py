# https://programmers.co.kr/learn/courses/30/lessons/42895
# 프로그래머스 코팅테스트 연습 > 동적계획법(Dynamic Programming) > N으로 표현
# 강의 내용


def solution(N, number):
    s = [set() for x in range(8)] # set()을 8개 만들어 각각 배열에 넣는다
    for i,x in enumerate(s, start=1): # 1부터 시작하는 enumerate를 사용 
        x.add(int(str(N)*i)) # 각 s의 각 set에 (int(str(N)*i)) 값을 넣는다
    for i in range(1, len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0: 
                        s[i].add(op1 // op2) # 정수 나눗셈

        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1

    return answer

N = 5
number = 12

print(solution(N,number))
