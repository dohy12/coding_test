import json
import requests
import time

host = "http://127.0.0.1:8000"

elevators = [{}]
distributor = 0

def onCall(token):
    headers = {"X-Auth-Token":token}
    return requests.get(host + "/oncalls", headers = headers).json()

def action(token, commands):
    # print(commands)
    headers = {"X-Auth-Token":token}
    requests.post(host + "/action", headers = headers, json=commands).json()
    return 


def getCall(token, call_info, call_lists):
    global elevators, distributor

    res = onCall(token)
    
    calls = res["calls"]
    elevators = res["elevators"]

    for c in calls:
        if c["id"] not in call_info:
            append_ch = False
            call_info[c["id"]] = {"start":c["start"], "end":c["end"], "timestamp":c["timestamp"], "upCheck":True if c["start"]<c["end"] else False}
            for call_list in call_lists:
                if (not append_ch):
                    for call in call_list:
                        if call_info[call]["start"] == call_info[c["id"]]["start"] and call_info[call]["upCheck"] == call_info[c["id"]]["upCheck"]:
                            call_list.append(c["id"])
                            append_ch = True
                            break

            if (not append_ch):
                call_lists[distributor].append(c["id"])
                distributor+=1
                if distributor >=4 :
                    distributor = 0


    return res["is_end"]
    

def solution(user_key):
    global host, elevators
    #start
    problem_id = 2
    elevators_num = 4
    res = requests.post(host+"/start"+"/"+user_key+"/"+str(problem_id)+"/"+str(elevators_num)).json()
    token = res["token"]

    call_info = {} # { 0 :{"start":0, "end":0, "timestamp":0, "upCheck":True} }
    call_lists = [[] for x in range(4)] # [ 0,1,2,3 ... ]   

    elevator_look = [0,0,0,0] # 0:UU, 1:UD, 2:DD, 3:DU 
    call_in_elevator = {}

    i = 0
    while True:   
        print(i)    
        if getCall(token, call_info, call_lists):
            print("finished")  
            break        
        
        # for call_list in call_lists:
        #     print("call:", [(k,v) for k,v in zip(call_info.keys(),call_info.values()) if k in call_list])

        i+=1
        commands = {"commands":[]}
        for e_idx in range(4):    
            # print("ele:",elevators[e_idx])
            enter_l = []
            exit_l  = [x["id"] for x in elevators[e_idx]["passengers"] if call_info[x["id"]]["end"] == elevators[e_idx]["floor"]]
            passengers_id = [x["id"] for x in elevators[e_idx]["passengers"]]

            if len(passengers_id)>0:
                
                call = call_info[passengers_id[0]]
                if call["upCheck"]: # 올라갈경우
                    elevator_look[e_idx] = 0
                    if len(passengers_id) < 8:
                        for call_id in call_lists[e_idx]:
                            tmp = call_info[call_id]
                            if tmp["upCheck"] and tmp["start"] == elevators[e_idx]["floor"]:
                                if call_id not in passengers_id and call_id not in enter_l and (len(enter_l)+len(passengers_id))<8:
                                    enter_l.append(call_id)
                
                else : # 내려갈 경우
                    elevator_look[e_idx] = 2
                    if len(passengers_id) < 8:
                        for call_id in call_lists[e_idx]:
                            tmp = call_info[call_id]
                            if (not tmp["upCheck"]) and tmp["start"] == elevators[e_idx]["floor"]:
                                if call_id not in passengers_id and call_id not in enter_l and (len(enter_l)+len(passengers_id))<8:
                                    enter_l.append(call_id)       
            else:
                if len(call_lists[e_idx])>0:
                    while True:
                        if elevator_look[e_idx] == -1:
                            elevator_look[e_idx] = 0
                        
                        if elevator_look[e_idx] == 0: #UU
                            tmp = 0
                            for call_id in call_lists[e_idx]:                        
                                call = call_info[call_id]
                                if call["upCheck"] and call["start"] >= elevators[e_idx]["floor"]:
                                    if call_id not in passengers_id:
                                        tmp = 1
                                if call["upCheck"] and call["start"] == elevators[e_idx]["floor"]:
                                    if call_id not in passengers_id and call_id not in enter_l and (len(enter_l)+len(passengers_id))<8:
                                        enter_l.append(call_id)

                            if tmp == 0:
                                elevator_look[e_idx] = 1
                            else:
                                break
                        

                        elif elevator_look[e_idx] == 1: #UD
                            tmp = 0
                            for call_id in call_lists[e_idx]:  
                                call = call_info[call_id]
                                if (not call["upCheck"]) and call["start"] > elevators[e_idx]["floor"]:
                                    if call_id not in passengers_id:
                                        tmp = 1
                                if (not call["upCheck"]) and call["start"] == elevators[e_idx]["floor"]:
                                    if call_id not in passengers_id and call_id not in enter_l and (len(enter_l)+len(passengers_id))<8:
                                        enter_l.append(call_id)

                                if call["upCheck"] and call["start"] >= elevators[e_idx]["floor"]:
                                    elevator_look[e_idx] = 0
                                    continue

                            if tmp == 0:
                                elevator_look[e_idx] = 2
                            else:
                                break
                    

                        elif elevator_look[e_idx] == 2: #DD
                            tmp = 0
                            for call_id in call_lists[e_idx]:  
                                call = call_info[call_id]
                                if (not call["upCheck"]) and call["start"] <= elevators[e_idx]["floor"]:
                                    if call_id not in passengers_id:
                                        tmp = 1
                                if (not call["upCheck"]) and call["start"] == elevators[e_idx]["floor"]:
                                    if call_id not in passengers_id and call_id not in enter_l and (len(enter_l)+len(passengers_id))<8:
                                        enter_l.append(call_id)

                            if tmp == 0:
                                elevator_look[e_idx] = 3
                            else:
                                break


                        elif elevator_look[e_idx] == 3: #DU
                            tmp = 0
                            for call_id in call_lists[e_idx]:  
                                call = call_info[call_id]
                                if (call["upCheck"]) and call["start"] < elevators[e_idx]["floor"]:
                                    if call_id not in passengers_id:
                                        tmp = 1
                                if (call["upCheck"]) and call["start"] == elevators[e_idx]["floor"]:
                                    if call_id not in passengers_id and call_id not in enter_l and (len(enter_l)+len(passengers_id))<8:
                                        enter_l.append(call_id)

                                if (not call["upCheck"]) and call["start"] <= elevators[e_idx]["floor"]:
                                    elevator_look[e_idx] == 2
                                    continue

                            if tmp == 0:
                                elevator_look[e_idx] = 0
                            else:
                                break         
                else:
                    elevator_look[e_idx] = -1
                    if elevators[e_idx]['status'] != 'OPENED':
                        commands["commands"].append({"elevator_id":e_idx, "command":"STOP"})
                    else:
                        commands["commands"].append({"elevator_id":e_idx, "command":"CLOSE"})
                    continue
           
            # ------------------------------------------------------
            if elevators[e_idx]['status'] == 'STOPPED':          

                if len(enter_l)>0 or len(exit_l)>0:
                    commands["commands"].append({"elevator_id":e_idx, "command":"OPEN"})
                elif elevator_look[e_idx] == 0 or elevator_look[e_idx] == 1:
                    commands["commands"].append({"elevator_id":e_idx, "command":"UP"})
                elif elevator_look[e_idx] == 2 or elevator_look[e_idx] == 3:
                    commands["commands"].append({"elevator_id":e_idx, "command":"DOWN"})
                else:
                    commands["commands"].append({"elevator_id":e_idx, "command":"STOP"})


            elif elevators[e_idx]['status'] == 'UPWARD':
                if len(enter_l)>0 or len(exit_l)>0:
                    commands["commands"].append({"elevator_id":e_idx, "command":"STOP"})
                elif elevator_look[e_idx] == 2 or elevator_look[e_idx] ==3:
                    commands["commands"].append({"elevator_id":e_idx, "command":"STOP"})
                elif elevator_look[e_idx] == 0 or elevator_look[e_idx] == 1:
                    commands["commands"].append({"elevator_id":e_idx, "command":"UP"})
                else :
                    commands["commands"].append({"elevator_id":e_idx, "command":"STOP"})


            elif elevators[e_idx]['status'] == 'DOWNWARD':
                if len(enter_l)>0 or len(exit_l)>0:
                    commands["commands"].append({"elevator_id":e_idx, "command":"STOP"})
                elif elevator_look[e_idx] == 0 or elevator_look[e_idx] ==1:
                    commands["commands"].append({"elevator_id":e_idx, "command":"STOP"})
                elif elevator_look[e_idx] == 2 or elevator_look[e_idx] ==3:
                    commands["commands"].append({"elevator_id":e_idx, "command":"DOWN"})
                else:
                    commands["commands"].append({"elevator_id":e_idx, "command":"STOP"})


            else: #엘베 opended   
                if  len(enter_l)>0:
                    commands["commands"].append({"elevator_id":e_idx, "command":"ENTER", "call_ids":enter_l}) 

                elif len(exit_l)>0:
                    commands["commands"].append({"elevator_id":e_idx, "command":"EXIT", "call_ids":exit_l}) 
                    for c in exit_l:
                        call_lists[e_idx].remove(c)                  
                else:
                    commands["commands"].append({"elevator_id":e_idx, "command":"CLOSE"}) 
            
        action(token, commands)         
        # print("---------------------------------------------------")
solution("tester")
