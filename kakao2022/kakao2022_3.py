import math

end_h = 23*60 + 59

def solution(fees, records):
    inout_h = {} # k 차번호, v: 들어간 시간
    rs_h = {}  # k 차번호, v: 누적주차 시간

    for r in records:
        r_l = r.split()
        h_l = r_l[0].split(":")
        h = int(h_l[0])*60 + int(h_l[1])

        if r_l[2] == "IN":
            inout_h[r_l[1]] = h
        else:
            in_h = inout_h[r_l[1]]
            out_h = h
            rs_h[r_l[1]] = rs_h.get(r_l[1],0) + (out_h-in_h)
            inout_h[r_l[1]] = -1
    
    for k,v in zip(inout_h.keys(),inout_h.values()):
        if v!=-1:
            in_h = inout_h[k]
            out_h = end_h
            rs_h[k] = rs_h.get(k,0) + (out_h-in_h)
        
        time = rs_h[k]
        fee = fees[1] + math.ceil(((time-fees[0]) if time>fees[0] else 0)/fees[2]) * fees[3]
        rs_h[k] = fee

    rs_h = [(k,v) for k,v in zip(rs_h.keys(),rs_h.values())]
    rs_h.sort()       

    answer = [x[1] for x in rs_h]
    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))
