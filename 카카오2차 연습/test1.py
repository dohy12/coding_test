import json
import requests
import time

host = "http://127.0.0.1:8000"

elevators = [{}]

def onCall(token):
    headers = {"X-Auth-Token":token}
    return requests.get(host + "/oncalls", headers = headers).json()

def action(token, commands):
    print(commands)
    headers = {"X-Auth-Token":token}
    print(requests.post(host + "/action", headers = headers, json=commands))
    return 


def getCall(token, call_info, call_list):
    global elevators

    res = onCall(token)
    calls = res["calls"]
    elevators = res["elevators"]

    for c in calls:
        if c["id"] not in call_info:
            call_info[c["id"]] = {"start":c["start"], "end":c["end"], "timestamp":c["timestamp"], "upCheck":True if c["start"]<c["end"] else False}
            call_list.append(c["id"])
    return res["is_end"]
    

def solution(user_key):
    global host, elevators
    #start
    problem_id = 0
    elevators_num = 1
    print("hi?2")
    res = requests.post(host+"/start"+"/"+user_key+"/"+str(problem_id)+"/"+str(elevators_num)).json()
    token = res["token"]

    call_info = {} # { 0 :{"start":0, "end":0, "timestamp":0, "upCheck":True} }
    call_list = [] # [ 0,1,2,3 ... ]   

    elevator_look = 0 # 0:UU, 1:UD, 2:DD, 3:DU 
    call_in_elevator = {}

    i = 0
    while i<40:    
        print(i)    
        if getCall(token, call_info, call_list):                    
            break        
        i+=1
        print(elevator_look, elevators)
        print("calls:",[(k,v) for k,v in zip(call_info.keys(), call_info.values()) if k in call_list])

        enter_l = []
        exit_l  = [x["id"] for x in elevators[0]["passengers"] if call_info[x["id"]]["end"] == elevators[0]["floor"]]
        
        passengers_id = [x["id"] for x in elevators[0]["passengers"]]

        if len(passengers_id)>0:
            call = call_info[passengers_id[0]]
            if call["upCheck"]: # 올라갈경우
                elevator_look = 0
                for call_id in call_list:
                    tmp = call_info[call_id]
                    if tmp["upCheck"] and tmp["start"] == elevators[0]["floor"]:
                        if call_id not in passengers_id:
                            enter_l.append(call_id)
            
            else : # 내려갈 경우
                elevator_look = 2
                for call_id in call_list:
                    tmp = call_info[call_id]
                    if (not tmp["upCheck"]) and tmp["start"] == elevators[0]["floor"]:
                        if call_id not in passengers_id:
                            enter_l.append(call_id)       
        else:
            while True:
                if elevator_look == 0: #UU
                    tmp = 0
                    for call_id in call_list:                        
                        call = call_info[call_id]
                        if call["upCheck"] and call["start"] >= elevators[0]["floor"]:
                            if call_id not in passengers_id:
                                tmp = 1
                        if call["upCheck"] and call["start"] == elevators[0]["floor"]:
                            if call_id not in passengers_id:
                                enter_l.append(call_id)

                    if tmp == 0:
                        elevator_look = 1
                    else:
                        break
                    

                elif elevator_look == 1: #UD
                    tmp = 0
                    for call_id in call_list:
                        call = call_info[call_id]
                        if (not call["upCheck"]) and call["start"] > elevators[0]["floor"]:
                            if call_id not in passengers_id:
                                tmp = 1
                        if (not call["upCheck"]) and call["start"] == elevators[0]["floor"]:
                            if call_id not in passengers_id:
                                enter_l.append(call_id)

                        if call["upCheck"] and call["start"] >= elevators[0]["floor"]:
                            elevator_look = 0
                            continue

                    if tmp == 0:
                        elevator_look = 2
                    else:
                        break
                

                elif elevator_look == 2: #DD
                    tmp = 0
                    for call_id in call_list:
                        call = call_info[call_id]
                        if (not call["upCheck"]) and call["start"] <= elevators[0]["floor"]:
                            if call_id not in passengers_id:
                                tmp = 1
                        if (not call["upCheck"]) and call["start"] == elevators[0]["floor"]:
                            if call_id not in passengers_id:
                                enter_l.append(call_id)

                    if tmp == 0:
                        elevator_look = 3
                    else:
                        break


                elif elevator_look == 3: #DU
                    tmp = 0
                    for call_id in call_list:
                        call = call_info[call_id]
                        if (call["upCheck"]) and call["start"] < elevators[0]["floor"]:
                            if call_id not in passengers_id:
                                tmp = 1
                        if (call["upCheck"]) and call["start"] == elevators[0]["floor"]:
                            if call_id not in passengers_id:
                                enter_l.append(call_id)

                        if (not call["upCheck"]) and call["start"] <= elevators[0]["floor"]:
                            elevator_look == 2
                            continue

                    if tmp == 0:
                        elevator_look = 0
                    else:
                        break
        
        # ------------------------------------------------------
        if elevators[0]['status'] == 'STOPPED':          

            if len(enter_l)>0 or len(exit_l)>0:
                action(token, {"commands":[{"elevator_id":0, "command":"OPEN"}]} )
            elif elevator_look == 0 or elevator_look == 1:
                action(token, {"commands":[{"elevator_id":0, "command":"UP"}]} )
            else:
                action(token, {"commands":[{"elevator_id":0, "command":"DOWN"}]} )

        elif elevators[0]['status'] == 'UPWARD':
            if len(enter_l)>0 or len(exit_l)>0:
                action(token, {"commands":[{"elevator_id":0, "command":"STOP"}]} )
            elif elevator_look == 2 or elevator_look ==3:
                action(token, {"commands":[{"elevator_id":0, "command":"STOP"}]} )
            else:
                action(token, {"commands":[{"elevator_id":0, "command":"UP"}]} )

        elif elevators[0]['status'] == 'DOWNWARD':
            if len(enter_l)>0 or len(exit_l)>0:
                action(token, {"commands":[{"elevator_id":0, "command":"STOP"}]} )
            elif elevator_look == 0 or elevator_look ==1:
                action(token, {"commands":[{"elevator_id":0, "command":"STOP"}]} )
            else:
                action(token, {"commands":[{"elevator_id":0, "command":"DOWN"}]} )

        else: #엘베 opended   
            if  len(enter_l)>0:
                action(token, {"commands":[{"elevator_id":0, "command":"ENTER", "call_ids":enter_l}]} )     

            elif len(exit_l)>0:
                action(token, {"commands":[{"elevator_id":0, "command":"EXIT", "call_ids":exit_l}]} )   
                for c in exit_l:
                    call_list.remove(c)                  
            else:
                action(token, {"commands":[{"elevator_id":0, "command":"CLOSE"}]} )
        print("----------------------")

solution("tester")
