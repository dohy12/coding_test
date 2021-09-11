# https://programmers.co.kr/learn/courses/30/lessons/42888
# 코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 오픈채팅방

def solution(record):
    h = {}

    st_ls = []
    for r in record:
        st_l = []
        l = r.split()

        if l[0] == "Enter":
            st_l.append(0)
            st_l.append(l[1])
            h[l[1]] = l[2]
        elif l[0] == "Leave":
            st_l.append(1)
            st_l.append(l[1])
        else :
            st_l.append(2)
            h[l[1]] = l[2]
        st_ls.append(st_l)
        

    answer = []
    for st_l in st_ls:
        if st_l[0] != 2: # chnage가 아닐경우
            if st_l[0] == 0: # enter
                st = h[st_l[1]] + "님이 들어왔습니다."        
            else :
                st = h[st_l[1]] + "님이 나갔습니다."      
            answer.append(st)
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))