import requests

x_auth_token = "c258e6b398b0ea36be57045c1250ed6a"

host = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"

def start():
    res  = requests.post(host+"/start", headers={"X-Auth-Token":x_auth_token}, json={"problem":1}).json()
    return res["auth_key"]

def getLocationInfo(auth_key):
    res = requests.get(host+"/locations",headers={"Authorization":auth_key}).json()
    return res

def getTruckInfo(auth_key):
    res = requests.get(host+"/trucks",headers={"Authorization":auth_key}).json()
    return res

def putSimpulate(auth_key, cmds):
    res = requests.put(host+"/simulate",headers={"Authorization":auth_key}, json={"commands":cmds}).json()
    return res

def getScore(auth_key):
    return requests.put(host+"/score",headers={"Authorization":auth_key}).json()

def locIDtoPos(location_id):
    return (int(location_id/5),location_id%5)

def isTruckWorking(truck_id):
    global truck_cmd_stack_real

    return len(truck_cmd_stack_real)>0

# 0: 6초간 아무것도 하지 않음
# 1: 위로 한 칸 이동
# 2: 오른쪽으로 한 칸 이동
# 3: 아래로 한 칸 이동
# 4: 왼쪽으로 한 칸 이동
# 5: 자전거 상차
# 6: 자전거 하차

def movTruck(truck, arrive_id):
    now = locIDtoPos(truck["location_id"])
    arrive = locIDtoPos(arrive_id)
    if arrive==now:
        return []

    cmd = []

    mov = (arrive[0] - now[0], arrive[1] - now[1])

    if (mov[0]!=0):
        if (mov[0]>0):
            cmd += [2 for x in range(abs(mov[0]))]
        else:
            cmd += [4 for x in range(abs(mov[0]))]
    if (mov[1]!=0):
        if (mov[1]>0):
            cmd += [1 for x in range(abs(mov[1]))]
        else:
            cmd += [3 for x in range(abs(mov[1]))]
    return cmd
    

truck_cmd_stack_real = [[] for x in range(5)]
truck_cmds_stack = [[] for x in range(5)]    
def solution1():
    global truck_cmd_stack_real
    global truck_cmds_stack

    auth_key = start()
    print(auth_key)

    # print(getLocationInfo(auth_key))

    trucks = getTruckInfo(auth_key)["trucks"]
    print(trucks)
    

    truck_origins = [6,8,16,17,12]
    # 각자 기본 위치로
    for i in range(5):
        truck_cmds_stack[i] += movTruck(trucks[i], truck_origins[i])

    # 각 location_ID에 트럭 할당하기
    truck_to_place = {} # truck_id 넣으면 place 반환
    place_to_truck = {} # place_id 넣으면 truck 반환

    for i in range(5):
        for x in range(3):
            for y in range(3):
                tmp = truck_origins[i] + 5 * (x-1) + (y-1)
                truck_to_place[i] = truck_to_place.get(i,[]) + [tmp]
                place_to_truck[tmp] = place_to_truck.get(tmp,[]) + [i]    

    print(truck_cmds_stack)
    ch =0
    while ch<1:
        ch += 1
        cmds = []
        for i in range(5):
            cmds.append({"truck_id":i, "command":truck_cmds_stack[i][:10]})
            truck_cmds_stack[i] = truck_cmds_stack[i][10:]
        
        res = putSimpulate(auth_key,cmds)
        
        locations = getLocationInfo(auth_key)

        for location in locations["locations"]:
            if location['located_bikes_count']<=2:          

                truck_list = place_to_truck(location['id']) # 관리하는 트럭 아이디 리스트

                work_truck_id = -1 # 일 시킬 트럭 id
                work_cnt = 999
                for t in truck_list:
                    if len(truck_cmd_stack_real)<work_cnt:
                        work_cnt = len(truck_cmd_stack_real)
                        work_truck_id = t # 가장 일 안하고 있는 트럭
                
                place_list = truck_to_place(t) # 현재 선택된 트럭이 관리하는 영역 list
                
                bike_place_list = sorted([(x["id"],x["located_bikes_count"]) for x in locations["locations"] if x["id"] in place_list],key=lambda x: x[1],reverse = True) 
                bike_needs = 4 - location['located_bikes_count'] # 부족한 바이크
                
                cnt = 0
                for b in bike_place_list:
                    if bike_needs == 0:
                        break
                    getBikes = min(bike_needs, b[1] - 4)
                    if getBikes>0:
                        cnt += getBikes
                        bike_needs += getBikes
                        locations["locations"][b[0]]['located_bikes_count'] -= getBikes
                        truck_cmd_stack_real.append(("mov",b[0]),("load",getBikes))

                if bike_needs>0:
                    
                
                if cnt>0:
                    truck_cmd_stack_real.append(("mov",location["id"]),("put", cnt))


        trucks = getTruckInfo(auth_key)["trucks"]

        if res["status"]=="finished":
            print(getScore(auth_key))
            break


solution1()