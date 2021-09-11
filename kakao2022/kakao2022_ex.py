def solution(v):
    h_x= {}
    h_y= {}
    for ch in v:
        h_x[ch[0]] = h_x.get(ch[0],0) + 1
        h_y[ch[1]] = h_y.get(ch[1],0) + 1
    
    x = -1
    for k,vl in zip(h_x.keys(), h_x.values()):
        if vl==1 :
            x = k
    y = -1
    for k,vl in zip(h_y.keys(), h_y.values()):
        if vl==1 :
            y = k
    answer = [x,y]
    return answer

v = [[1, 4], [3, 4], [3, 10]]
