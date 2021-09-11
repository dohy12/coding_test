# https://programmers.co.kr/learn/courses/30/lessons/72411
# 코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 메뉴 리뉴얼

def solution(orders, course):
    ob_l = [] # order bit list
    for o in orders:
        order_b = 0 
        for s in o:
            order_b += pow(2,ord(s) - ord('A'))
        ob_l.append(order_b)

    rs_s = set([])
    for i, o1 in enumerate(ob_l):
        for j, o2 in enumerate(ob_l[i+1:],start=(i+1)):
            rs_s.update([o1&o2])
    
    rs_l = []
    for s in rs_s:
        st = ""
        for i in range(26):
            if (s&pow(2,i))>0:
                st += chr(ord('A') + i)
        if len(st) in course:
            rs_l.append(st)
    rs_l.sort()
    return rs_l
    
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))