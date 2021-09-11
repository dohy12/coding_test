def solution(info, edges):
    e_h = {}
    for e in edges:
        e_h[e[0]] = e_h.get(e[0],[]) + [e[1]]

    max_sheep = 0

    r_idx =0 
    stack = [r_idx] 
    route_h = {r_idx:[0,0,[0]]} # [0]:sheep , [1]:wolf, [2]:route

    info_n = len(info)
    while stack:
        p_idx = stack.pop()
        now_pos = route_h[p_idx][2][-1]
        route_h[p_idx][info[now_pos]]+=1
        if (route_h[p_idx][0] > max_sheep):
            max_sheep = route_h[p_idx][0]
        if route_h[p_idx][0] > route_h[p_idx][1]:
            if len(route_h[p_idx][2]) == info_n:
                break
            cango_l = []
            for r in route_h[p_idx][2]:
                e_l = e_h.get(r,[])
                for e in e_l:
                    if e not in route_h[p_idx][2]:
                        cango_l.append(e)
            
            for c_r in cango_l:
                r_idx +=1
                tmp_r = list(route_h[p_idx][2])
                tmp_r.append(c_r)
                route_h[r_idx] = [route_h[p_idx][0], route_h[p_idx][1], tmp_r]
                stack.append(r_idx)          

    answer = max_sheep
    return answer
    

info  = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

print(solution(info, edges))