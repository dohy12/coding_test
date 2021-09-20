import requests
from collections import deque

host = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
x_auth_token = "89f497622f57784596ae13ec7468b244"

box_size = 5
truck_num = 5

def start(problem):
    return requests.post(host+"/start",headers={'X-Auth-Token':x_auth_token}, json={"problem":problem}).json()["auth_key"]

def getLocations(auth_key):
    return requests.get(host+"/locations",headers={'Authorization':auth_key}).json()

def getTrucks(auth_key):
    return requests.get(host+"/trucks",headers={'Authorization':auth_key}).json()

def pos_to_locID(pos):
    return pos[0]*5 + pos[1]

def locID_to_pos(locID):
    return [int(locID/box_size),locID%box_size]

def cmd_str_to_real(trucks, trucks_cmds_queue_str, trucks_cmds):
    for i in range(truck_num):
        truck = trucks[i]
        queue_str = trucks_cmds_queue_str[i]
        trucks_cmd = trucks_cmds[i]
        
        while len(queue_str)>0:
            tmp = []
            st = queue_str.popleft()

            if st[0] == "load":            
                tmp += [5 for x in range(st[1])]
            elif st[0] == "land":
                tmp += [6 for x in range(st[1])]
            elif st[0] == "go":
                tmp += cmd_go(trucks[i]["arrive"],st[1])
                trucks[i]["arrive"] = st[1]

            trucks_cmd += tmp
    return            
    
def cmd_go(arrive, to):
    cmds = []
    arrive_pos = locID_to_pos(arrive)
    to_pos = locID_to_pos(to)

    if to_pos[0] > arrive_pos[0]:
        cmds += [2] * (to_pos[0]-arrive_pos[0])
    else :
        cmds += [4] * (arrive_pos[0]-to_pos[0])

    if to_pos[1] > arrive_pos[1]:
        cmds += [1] * (to_pos[1]-arrive_pos[1])
    else :
        cmds += [3] * (arrive_pos[1]-to_pos[1])

    return cmds

def putSimulate(auth_key, cmds):
    json = []
    for idx, cmd in enumerate(cmds):
        json.append( {"truck_id":idx, "command":cmd} )
    
    res = requests.put(host + "/simulate",headers={"Authorization":auth_key},json={"commands":json}).json()
    print("time:",res["time"])
    return res["status"]

def getScore(auth_key):
    return requests.get(host+"/score",headers={'Authorization':auth_key}).json()

def truck_work(truck, work_list, to_loc_ID, locations):
    cmd_str = []

    work_list_reversed = reversed(work_list)

    need_bikes = 4 - locations[to_loc_ID]["located_bikes_count"]
    bikes = truck["loadedBikes"]
    for work in work_list_reversed:
        if bikes>=need_bikes:
            break
        if work[1]>4:
            bikes += 2
            locations[work[0]]["located_bikes_count"] -= 2
            cmd_str +=[("go",work[0]),("load",2)]
        else:
            break

    # to_loc_id 주변
    arround_loc_list = []
    for y in range(3):
        for x in range(3):
            tmp = to_loc_ID + (x-1)*5 + (y-1)
            if tmp>=0 and tmp<=24:
                arround_loc_list.append(tmp)
    
    for arround_id in arround_loc_list:
        if bikes>=need_bikes:
            break
        if locations[arround_id]["located_bikes_count"] == 4:
            bikes +=1
            locations[arround_id]["located_bikes_count"] -= 1
            cmd_str +=[("go",arround_id),("load",1)]

    if(bikes>0):
        cmd_str +=[("go",to_loc_ID),("land", min(bikes,need_bikes))]
        locations[to_loc_ID]["located_bikes_count"] += min(bikes,need_bikes)

    return cmd_str

def sol1():
    auth_key = start(1)

    trucks = [{"id":x, "pos":0, "loadedBikes":0, "arrive":0} for x in range(truck_num)] 
    trucks_cmds = [[] for x in range(truck_num)]
    trucks_cmds_queue_str = [deque([]) for x in range(truck_num)] # [("go",locID),("load",2),("land",2)]

    trucks_origin_pos = [6,8,16,18,12]
    trucks_work_range = [[] for x in range(truck_num)]

    # 트럭 기본 설정 (기본 위치로 이동, 트럭 범위 지정)
    for idx in range(truck_num):
        trucks_cmds_queue_str[idx] += [("go",trucks_origin_pos[idx])] + [("load",1)]
        for y in range(3):            
            for x in range(3):
                trucks_work_range[idx] += [trucks_origin_pos[idx] + (x - 1) *5 + (y - 1)]   

    while True:
        cmd_str_to_real(trucks, trucks_cmds_queue_str, trucks_cmds) 
        # print(trucks_cmds)
        # 명령 10개 단위로 짜르기
        tmp_cmd = []
        for idx in range(truck_num):
            tmp_cmd.append(trucks_cmds[idx][:10])
            trucks_cmds[idx] = trucks_cmds[idx][10:]

        # 명령 실행
        if putSimulate(auth_key, tmp_cmd)=="finished":
            print(getScore(auth_key))
            break

        locations = getLocations(auth_key)["locations"]
        truck_tmp = getTrucks(auth_key)["trucks"]

        # print("--loc: ",locations)
        # print("--trucks: ",trucks)

        for idx in range(truck_num):
            trucks[idx]["pos"] = truck_tmp[idx]["location_id"]
            trucks[idx]["loadedBikes"] = truck_tmp[idx]["loaded_bikes_count"]
        
        for idx in range(truck_num):
            work_list = sorted([(x,locations[x]["located_bikes_count"]) for x in trucks_work_range[idx]],key=lambda x:x[1])

            for work in work_list:
                if work[1]<=2:
                    trucks_cmds_queue_str[idx] += truck_work(trucks[idx], work_list, work[0], locations)
                
        # print(trucks_cmds_queue_str)

        # print("------------------------------------------")


sol1()