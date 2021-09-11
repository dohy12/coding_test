# https://programmers.co.kr/learn/courses/30/lessons/43165
# 프로그래머스 코팅테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 타겟 넘버

def solution(numbers, target):
    l = [numbers[0],-numbers[0]]
    
    for n in numbers[1:]:
        l2 = []
        for i in range(len(l)):
            l2.append(l[i] + n)
            l2.append(l[i] - n)
        l = l2

    cnt =0
    for n in l:
        if n == target:
            cnt +=1
            
    answer = cnt
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))