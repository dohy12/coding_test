# https://programmers.co.kr/learn/courses/30/lessons/42862
# 프로그래머스 코팅테스트 연습 > 탐욕법(Greedy) > 큰 수 만들기
# 강의 풀이

def solution(number, k):
    collected = []
    for i, num in enumerate(number): # enumerate 튜플로 (index, num)값을 넘겨준다.
        while len(collected) > 0 and collected[-1] < num and k > 0: # 마지막 글자 체크할때 collected[-1]로 체크 가능
            collected.pop()
            k-=1
        if k==0:
            collected += list(number[i:])
            break
        collected.append(num)
    collected = collected[:-k] if k>0 else collected
    answer = ''.join(collected)
    return answer
            
number = "4177252841"
k = 4
print(solution(number, k))