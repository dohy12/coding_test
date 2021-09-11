# https://programmers.co.kr/learn/courses/30/lessons/60057
# 코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT > 문자열 압축

def solution(s):
    m_l = 999999999999999999999
    for s_idx in range(1,len(s)+1): #slice_idx
        l = []
        for w_idx in range(0, len(s),s_idx):
            l.append(s[w_idx:w_idx+s_idx])

        idx = 0
        cnt_l = []
        while True:
            if idx >= len(l):
                break
            ch = l[idx]
            ch_idx = idx + 1
            cnt = 1
            while ch_idx<len(l) and ch == l[ch_idx]:
                cnt+=1
                l.pop(ch_idx)
            if cnt !=1:
                cnt_l.append(str(cnt))
            idx+=1
        
        st = ''.join(l+cnt_l)
        print(st)
        m_l = min(m_l, len(st))
        
    answer = m_l
    return answer

s = "xxxxxxxxxxyyy"
print(solution(s))