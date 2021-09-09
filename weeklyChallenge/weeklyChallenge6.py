# https://programmers.co.kr/learn/courses/30/lessons/85002
# 프로그래머스 코팅테스트 연습 > 위클리 챌린지 > 6주차
# 한번에 성공! ㅋㅋㅋ

def solution(weights, head2head):    
    l = [[0,0,0,x,i] for i,x in enumerate(weights)] # [f_cnt, f_w, f_b, w, idx]

    for i,fights in enumerate(head2head):
        for j,f in enumerate(fights[i:],start = i):
            w_idx = l_idx = -1
            if f != 'N':
                l[i][0] += 1
                l[j][0] += 1

                w_idx = i if f =='W' else j
                l_idx = i if f =='L' else j

                l[w_idx][1] += 1
                l[w_idx][2] += 1 if l[w_idx][3] < l[l_idx][3] else 0       

    l.sort(key=lambda x:(x[1]/x[0] if x[0]>0 else 0,x[2],x[3],-x[4]),reverse=True)

    answer = [x[4]+1 for x in l]
    return answer


weights = [50,82,75,120]
head2head = ["NLWL","WNLL","LWNW","WWLN"]
print(solution(weights, head2head))

weights = [145,92,86]
head2head = ["NLW","WNL","LWN"]
print(solution(weights, head2head))