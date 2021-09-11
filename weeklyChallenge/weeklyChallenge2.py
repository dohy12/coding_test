# https://programmers.co.kr/learn/courses/30/lessons/82612
# 프로그래머스 코팅테스트 연습 > 위클리 챌린지 > 2주차

def getScoreStr(score):
    if score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif score>=70:
        return 'C'
    elif score>=50:
        return 'D'
    else:
        return 'F'

def solution(scores):
    n = len(scores)
    students = [[0]*n for x in range(n)]

    for y,s in enumerate(scores):
        for x,s_value in enumerate(s):
            students[x][y] = s_value

    rs = ""
    for idx,s in enumerate(students):
        if s[idx]==max(s) or s[idx]==min(s):
            cnt =0
            for tmp in s:
                if tmp == s[idx]:
                    cnt+=1
            if cnt==1:
                s.pop(idx)
            students[idx] = s

        rs+= getScoreStr(sum(s)/len(s))

    answer = rs
    return answer

scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
print(solution(scores))