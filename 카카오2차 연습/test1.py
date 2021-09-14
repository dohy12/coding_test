import json
import requests

host = "http://127.0.0.1:8000"


# 엘베 상태
# 1) 엘베 stopped
#   if) 현재 층에 내릴 사람 존재 or 현재 층에 탈 사람 존재
#       action open
#   elif) 이전 상태 : upward
#       action up
#   elif) 이전 상태 : downward   
#       action down

# 2) 엘베 upward
#   if) 현재 층에 내릴 사람 존재 or 현재 층에 탈 사람 존재
#       action stop
#   else:
#       action up 

# 3) 엘베 downward

# 4) 엘베 opended
#   if) 현재 층에 내릴 사람 존재
#       action Exit
#   elif) 현재 층에 탈 사람 존재
#       action Enter
#   else: 내릴 사람도 탈 사람도 없을때:
#       action close

def onCall(token):
    headers = {"X-Auth-Token":token}
    return requests.get(host + "/oncalls", headers = headers).json()

def action(token, commands):
    headers = {"X-Auth-Token":token}
    return requests.get(host + "/oncalls", headers = headers, json=commands).json()


def getCall(token, call_info, call_list):
    calls = onCall(token)["calls"]

    for c in calls:
        if c["id"] not in call_info:
            call_info[c["id"]] = {"start":c["start"], "end":c["end"], "timestamp":c["timestamp"]}
            call_list.append(c["id"])
    return
    

def solution(user_key):
    global host
    #start
    problem_id = 0
    elevators_num = 1
    res = requests.post(host+"/start"+"/"+user_key+"/"+str(problem_id)+"/"+str(elevators_num)).json()
    token = res["token"]

    call_info = {} # { 0 :{"start":0, "end":0, "timestamp":0} }
    call_list = [] # [ 0,1,2,3 ... ]   
    print(call_info,call_list)

    while True:
        getCall(token, call_info, call_list)

        call_cnt = getCall(token,call_info,call_list, call_cnt)
        
        action(token, "up")
        

solution("tester")