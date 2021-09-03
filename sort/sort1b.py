# https://programmers.co.kr/learn/courses/30/lessons/42746
# 프로그래머스 코팅테스트 연습 > 정렬(sort)) > 가장 큰수
# 이준성님 풀이

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True) # functools.cmp_to_key(comparator) comparator함수를 key로 사용해서 sort한다.
    answer = str(int(''.join(n)))   # ''.join(n)을하면 각 문자열들을 전부 합쳐서 하나의 문자열을 출력해줌 '_'.join(str)하면 a_b_c이렇게 됨 '구분자'.join(문자열배열)
                                    # 그 후 int()를 통해 00000 -> 0으로 변환 해준다.
    return answer

numbers = [0,0,0,0]
print(solution(numbers))