# https://programmers.co.kr/learn/courses/30/lessons/42746
# 프로그래머스 코팅테스트 연습 > 정렬(sort)) > K번째수

def solution(array, commands):
    answer = []
    for c in commands:
        arr = array[c[0]-1:c[1]]
        arr.sort()
        answer.append(arr[c[2]-1])
    
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))