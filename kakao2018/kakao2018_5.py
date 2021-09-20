# https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3
# 코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > 추석 트래픽

def time_to_tuple(time_info):
    time_str = time_info[1].replace(".", "")
    time_str2 = time_info[2].replace(".", "")[:-1]
    time_str2 = time_str2 + '0' * (4 - len(time_str2))

    time_slice = [int(x) for x in time_str.split(':')]
    time_span = int(time_str2)

    end_time = time_slice[0] * 60*60*1000 + time_slice[1] * 60*1000 + time_slice[2]
    start_time = end_time - time_span + 1 
    
    return (start_time if start_time>0 else 0, end_time)

def solution(lines):
    times = [(idx,time_to_tuple(x.split())) for idx,x in enumerate(lines)]
    max_len = len(times)
    max_cnt = 0

    print(times)

    for time in times:
        back_time = time[1][1] 
        t_idx  = time[0]
        s = set()

        while t_idx < max_len:
            time_tmp = times[t_idx]
            if(time_tmp[1][1]<=back_time+999):
                s.add(time_tmp[0])                
            else:
                break
            t_idx+=1
        
        while t_idx < max_len:
            time_tmp = times[t_idx]
            if (time_tmp[1][1])>=back_time+3000:
                break

            if (time_tmp[1][0]<=back_time+999):
                s.add(time_tmp[0])
            t_idx+=1

        max_cnt = max(max_cnt,len(s))
        
    answer = max_cnt
    return answer


lines =  [
"2016-09-15 23:59:58.000 1.000s",
"2016-09-15 23:59:60.000 1s"
]
print(solution(lines))