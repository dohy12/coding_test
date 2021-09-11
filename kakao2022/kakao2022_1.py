
def solution(id_list, report, num):
    used = {}
    reported_l = [[] for x in id_list]

    h = {}
    for idx, u_id in enumerate(id_list):
        h[u_id] = idx

    print(h)

    for r in report:
        r_l = r.split()
        if used.get((r_l[0],r_l[1]),0) == 0:
            used[(r_l[0],r_l[1])] = 1
            reported_l[ h[r_l[1]] ].append(r_l[0])
    
    answer = [0 for x in id_list]
    print(reported_l)
    for idx,l in enumerate(reported_l):
        if (len(l)>=num):
            for em in l:
                answer[h[em]]+=1

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))