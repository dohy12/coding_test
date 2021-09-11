# https://programmers.co.kr/learn/courses/30/lessons/81301
# 코딩테스트 연습 > 2021 카카오 채용연계형 인턴십 > 숫자 문자열과 영단어

h = {
    "zero" : "0",
    "one" : "1",
    "two" : "2",
    "three": "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

def solution(s):
    for k,v in zip(h.keys(), h.values()):
        s = s.replace(k,v)

    answer = s
    return int(answer)


s = "one4seveneight"
print(solution(s))