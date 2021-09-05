

for i in range(0,20):
    l = [2] * i + [3] + [2] * (19-i)
    print(l)

    calc_time = 0
    all_time = 0 
    cnt2 = 0
    for j in l:
        all_time += j
        if j == 2:
            calc_time += (all_time- (2+cnt2))
            cnt2+=1
        else:
            calc_time += (all_time - 1)
    
    print(calc_time, all_time)