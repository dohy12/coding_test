# https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3
# 프로그래머스 코팅테스트 연습 > 탐욕법(Greedy) > 조이스틱
name = "ABBAAAAAAAAAB"

aaa_check = 0
for i in name:
    if(i!='A'):
        aaa_check+=1

if(aaa_check==0):
    print(0)

tupple_list = []
t_s = -1

for i in range(1, len(name)+1):
    if(i == len(name)):
        if(t_s!=-1):
            t_e = i - 1
            tupple_list.append( (t_s,t_e) )
        break
    else:
        if (name[i] == 'A'):
            if(t_s != -1):
                t_e = i - 1
                tupple_list.append( (t_s,t_e) )
                t_s = -1
        else :
            if(t_s == -1):
                t_s = i

print(tupple_list)
m_min = 99
mv = 999
for i in range(0, len(tupple_list) + 1):
    l_max = 0
    r_min = len(name)

    if(len(tupple_list) - 1 - i >=0):
        l_max = tupple_list[len(tupple_list) - 1 - i][1]        
    else:
        l_max = 0 
    
    if((len(tupple_list)-i)<len(tupple_list)):
        r_min = tupple_list[len(tupple_list)-i][0]        
    else:
        r_min = len(name) 

    r_len = len(name) - r_min

    print(l_max, r_len)
    mv = min(min(l_max, r_len) * 2 + max(l_max, r_len),mv)
    

name_mv = 0
for i in name:
    chmv = min((ord(i)-ord('A')),(ord('Z')-ord(i)+1))
    name_mv += chmv


print(name_mv+mv)

##정답