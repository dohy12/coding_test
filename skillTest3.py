import functools

def solution(s):
    s = s[2:-2] # 양쪽 대 괄호 제거
    s_l = s.split('},{')

    h = {}
    for st in s_l:
        tmp_l = st.split(',')
        h[len(tmp_l)] = set([int(x) for x in tmp_l])
    
    rs_l = []
    for i in range(1, len(s_l)+1):
        rs_l += list(h[i] - set(rs_l))

    return rs_l

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"

print(solution(s))