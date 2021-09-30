# 아무것도 안했을때
import requests

x_auth_token = "20c89c1e79fc79a14f27037ffb115966"
host = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"

box_size = 5
truck_cnt = 5

def start():
    res  = requests.post(host+"/start", headers={"X-Auth-Token":x_auth_token}, json={"problem":1}).json()
    return res["auth_key"]

def putSimpulate(auth_key):
    res = requests.put(host+"/simulate",headers={"Authorization":auth_key}, json={"commands":[]}).json()
    print("time:",res["time"])
    return res["status"]

def getScore(auth_key):
    return requests.get(host+"/score",headers={'Authorization':auth_key}).json()

def getLocation(auth_key):
    return requests.get(host+"/locations",headers={'Authorization':auth_key}).json()

def getTrucks(auth_key):
    return requests.get(host+"/trucks",headers={'Authorization':auth_key}).json()

def setCmds(auth_key, locations, trucks):    
    cmds = [[] for x in range(truck_cnt)]

    locations.sort(key=lambda x:x["located_bikes_count"])

    for location in locations:    
        if location["located_bikes_count"]<=1:
            nearestTruck = getNearestTruck(location["id"],trucks,cmds)
            if nearestTruck[0] != -1:
                
            else:
                break
        else:
            break
    
def getDistance(loc_id_from,loc_id_to):
    x = (loc_id_to-loc_id_from)//5
    y = (loc_id_to-loc_id_from)%5
    return x + y

def getNearestTruck(loc_id_from, trucks, cmds):
    tmp = sorted([(x["id"],getDistance(loc_id_from, x["location_id"])) for x in trucks if len(cmds[x["id"]])==0],key=lambda x:x[1])
    return tmp[0] if len(tmp)>0 else (-1,0)
    



def sol1():
    
    auth_key = start()

    while True:
        locations = getLocation(auth_key)["locations"]
        trucks = getTrucks(auth_key)["trucks"]

        cmds = []



    


sol1()