# https://programmers.co.kr/learn/courses/30/lessons/67256
# 코딩테스트 연습 > 2020 카카오 인턴십 > 키패드 누르기

# 0 = (0,0)
# * = (-1,0)
# # = (1,0)

import math

def solution(numbers, hand):
    l_pos = (-1,0)
    r_pos = (1,0)

    ch_l = [1,4,7]
    ch_r = [3,6,9]

    ans = ""
    for n in numbers:        
        if n in ch_l:
            l_pos = (-1, math.ceil((10-n)/3))
            ans += "L"
        elif n in ch_r:
            r_pos = (1, math.ceil((10-n)/3))
            ans += "R"
        else :
            goal_pos = (0, math.ceil((10-n)/3) if n!=0 else 0)
            l_dis = abs(l_pos[0] - goal_pos[0]) + abs(l_pos[1] - goal_pos[1])
            r_dis = abs(r_pos[0] - goal_pos[0]) + abs(r_pos[1] - goal_pos[1])
            if l_dis<r_dis:
                l_pos = goal_pos
                ans+="L"
            elif l_dis>r_dis:
                r_pos = goal_pos
                ans+="R"
            else :
                if hand == "left":
                    l_pos = goal_pos
                    ans+="L"
                else :
                    r_pos = goal_pos
                    ans+="R"

    return ans


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))