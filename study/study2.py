# https://programmers.co.kr/learn/courses/30/lessons/43236
# 코딩테스트 연습 > 이분탐색> 징검다리

def solution(distance, rocks, n):
    rocks.sort()

    len_list = [rocks[0]] + [b-f for f,b in zip(rocks[:-1],rocks[1:])] + [distance - rocks[-1]]

    return binary(1, distance, len_list, n)

def binary(left, right, len_list, n):
    mid = int((left + right)/2)
    tmp_list = list(len_list)

    idx = 0
    removed_rock = 0
    while (idx<len(tmp_list)):
        if len(tmp_list) == 1:
            break

        if tmp_list[idx] < mid:
            removed_rock+=1
            
            if idx == 0:
                tmp_list[idx+1] = tmp_list[idx] + tmp_list[idx+1]
                tmp_list.pop(idx)
            elif idx == len(tmp_list)-1:
                tmp_list[idx-1] = tmp_list[idx] + tmp_list[idx-1]
                tmp_list.pop(idx)
            else :
                left_dis = tmp_list[idx-1]
                right_dis = tmp_list[idx+1]

                if left_dis> right_dis:
                    tmp_list[idx+1] = tmp_list[idx] + tmp_list[idx+1]
                    tmp_list.pop(idx)
                else:
                    tmp_list[idx-1] = tmp_list[idx] + tmp_list[idx-1]
                    tmp_list.pop(idx)
        else:
            idx += 1
    
    if removed_rock > n:
        return binary(left, mid-1, len_list, n)
    elif removed_rock < n:
        return binary(mid+1, right, len_list, n)
    else :
        tmp_list.sort()
        return tmp_list[0]
        


distance = 25
rocks = [2,5,10]
n = 1

print(solution(distance, rocks, n))