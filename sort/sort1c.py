# https://programmers.co.kr/learn/courses/30/lessons/42746
# 프로그래머스 코팅테스트 연습 > 정렬(sort)) > 가장 큰수
# 강의

def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers = sorted(numbers, key=lambda x:(x*4)[:4], reverse=True)

    answer = str(int(''.join(numbers)))
    return answer

numbers = [1,12,42,10]
print(solution(numbers))