# https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3
# 프로그래머스 코팅테스트 연습 > 탐욕법(Greedy) > 조이스틱
# [신동주]님의 풀이 공부

def solution(name):
    answer = 0
    n = len(name)
    num_char = [i for i in range(14)] + [i for i in range(12, 0, -1)] # 문자열 변환을 미리 배열로 만들어 둔다.

    for ch in name:
        answer += num_char[ord(ch) - ord('A')]

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1

        while (next_idx < n) and (name[next_idx] == 'A'): # 바로 다음 A가 아닌 것을 찾는다.
            next_idx += 1 
            
        distance = min(idx, n - next_idx) # 왼쪽 오른쪽 중 더 가까운 것을 찾는다.
        move = min(move, idx + n - next_idx + distance) # 가까운거 *2 + 먼거

    answer += move
    return answer


print(solution("ABBAAAAAB"))