
def solution(n, info):
    max_l = []
    max_n = 0

    r_idx = 0
    stack = []
    route_h = {}
    if n >= info[0]+1:
        route_h[r_idx] = ([10],1,n-(info[0]+1))
        stack.append(r_idx)
        r_idx +=1
        
    route_h[r_idx] = ([],1,n) # r_info[0] : route , r_info[1] : idx, r_info[2] : remainedArr
    stack.append(r_idx)
    r_idx +=1

    while stack:
        p_idx = stack.pop()
        r_info = route_h[p_idx]

        now_idx = r_info[1]
        if now_idx < 11:
            r_idx +=1
            route_h[r_idx] = (list(r_info[0]), now_idx+1 , r_info[2]) # 이번 점수는 패스
            stack.append(r_idx)
            if (r_info[2] >= (info[now_idx]+1)): # 남은 화살이 현재 점수 아파치 화살 보다 많을경우
                r_idx +=1
                tmp = list(r_info[0])
                tmp.append(10 - now_idx)
                route_h[r_idx] = (tmp, now_idx+1 , r_info[2]-(info[now_idx]+1)) # 이번 점수 얻기
                stack.append(r_idx)
        else:
            score1 = sum(r_info[0]) if len(r_info[0])>0 else 0
            score2 = 0
            for idx, i in enumerate(info):
                if i>0 and (10-idx) not in r_info[0]:
                    score2 += (10-idx)
            if (score1>score2):
                ch_n = score1-score2

                if ch_n > max_n:
                    max_n=ch_n
                    max_l = [(r_info[2],r_info[0])]
                elif ch_n == max_n:                    
                    max_l.append((r_info[2],r_info[0]))

    rs_ls = [] 
    if len(max_l)>0:
        for l in max_l:
            tmp_l = [0 for x in range(11)]
            for i in l[1]:
                tmp_l[10-i] = info[10-i] +1
            
            tmp_l[10] += l[0]
            tmp_l.reverse()
            rs_ls.append(tmp_l)

        rs_ls.sort(reverse=True)
        rs_ls[0].reverse()
        answer = rs_ls[0]
    else:
        answer = [-1]
    return answer

n = 1
info = [1,0,0,0,0,0,0,0,0,0,0]

print(solution(n, info))