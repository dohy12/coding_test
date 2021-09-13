import json
import requests

host = "http://127.0.0.1:8000"



# 엘베 상태
# 1) 엘베 stop
#   - deque에서 timestamp가 젤 작은 애들 확인해보고 젤 가까운 call 실행
#   - 

# 2) 엘베 upward

# 3) 엘베 downward

# 4) 엘베 opended

def onCall(token):
    headers = {"X-Auth-Token":token}
    return requests.get(host + "/oncalls", headers = headers).json()

def action(token, commands):
    headers = {"X-Auth-Token":token}
    return requests.get(host + "/oncalls", headers = headers, json=commands).json()


def getCall(token, call_info, call_list, call_cnt):
    calls = onCall(token)["calls"]

    for c in calls:
        if c["id"] not in call_info:
            call_cnt+=1
            call_info[c["id"]] = {"start":c["start"], "end":c["end"], "timestamp":c["timestamp"]}
            call_list.append(c["id"])
    return call_cnt

def solution(user_key):
    global host
    #start
    problem_id = 0
    elevators_num = 1
    res = requests.post(host+"/start"+"/"+user_key+"/"+str(problem_id)+"/"+str(elevators_num)).json()
    token = res["token"]

    call_info = {}
    call_list = []
    call_cnt = 0
    call_cnt = getCall(token,call_info,call_list, call_cnt)
    print(call_info,call_list)

    # while not (call_cnt==6):        
    #     call_cnt = getCall(token,call_info,call_list, call_cnt)
        
    #     action(token, "up")
        

solution("tester")