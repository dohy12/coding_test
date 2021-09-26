# https://programmers.co.kr/learn/courses/30/lessons/42587
# 프로그래머스 코딩테스트 연습 > 스택/큐 > 프린터


# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.

def isInStack(doc, stack):
    for v in stack:
        if v[1] > doc:
            return True
    return False

def solution(priorities, location):
    stack = [(idx,v) for idx,v in enumerate(priorities)]
    cnt = 0
    while stack:
        doc = stack.pop(0)
        if isInStack(doc[1],stack):
            stack.append(doc)
        else:
            cnt += 1
            if doc[0] ==location:
                return cnt
    return -1

priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))