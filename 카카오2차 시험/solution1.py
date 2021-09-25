import requests

x_auth_token = "395e027902beeba119a06c67c14f9a97"
host = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"

player_cnt = 30

def start():
    res  = requests.post(host+"/start", headers={"X-Auth-Token":x_auth_token}, json={"problem":1}).json()
    return res["auth_key"]

def getWaitingLine(auth_key): # 현재 대기열에서 매칭을 대기 중인 유저들의 정보를 반환한다. { "id": 1, "from": 3 }
    res = requests.get(host+"/waiting_line",headers={"Authorization":auth_key}).json()
    return res

def getGameResult(auth_key): # 이번 턴에 게임이 끝난 유저들의 게임 결과를 반환한다. {"win": 10, "lose": 2, "taken": 7 },
    res = requests.get(host+"/game_result",headers={"Authorization":auth_key}).json()
    return res

def getUserInfo(auth_key): # 모든 유저들의 현재 등급을 반환한다. { "id": 1, "grade": 2100 },
    res = requests.get(host+"/user_info",headers={"Authorization":auth_key}).json()
    return res

def putMatch(auth_key,pairs):
    res = requests.put(host+"/match",headers={"Authorization":auth_key},json={"pairs":pairs}).json()
    return res

def putChangeGrade(auth_key,cmds):
    res = requests.put(host+"/change_grade",headers={"Authorization":auth_key},json={"commands":cmds}).json()
    return res

def getScore(auth_key):
    res = requests.get(host+"/score",headers={"Authorization":auth_key}).json()
    return res

def calcMMR(time): # 40분 게임 시 서로 mmr 25증감 3분 게임 시 서로 50증감 
    return (-1.35*time + 104)/2

def setWaitingTier(lines, mmrs):
    tmp = {}
    for line in lines:
        mmr = mmrs[line["id"]]
        tmp[(mmr//100)*100] = tmp.get((mmr//100)*100,[]) + [line["id"]]
    return tmp

def setMatching(lines, mmrs, players_tiers):
    pairs = []

    matched = {}
    for line in lines:
        if not matched.get(line["id"],False):
            mmr = (mmrs[line["id"]]//100)*100

            opponent_id = -1
              
            for i in range(3):
                if opponent_id != -1:
                    break
                if line["from"] >= 4*i:
                    can_match_list = set([])
                    can_match_list.update(players_tiers.get(mmr+100*i,[]))
                    can_match_list.update(players_tiers.get(mmr-100*i,[]))

                    can_match_list = sorted([(x,abs(mmrs[line["id"]]-mmrs[x])) for x in can_match_list],key=lambda x:x[1])

                    for player_id in can_match_list:
                        if line["id"] != player_id[0]:
                            opponent_id = player_id[0]
                            break            

            if opponent_id != -1:
                pair = [line["id"], opponent_id]
                pairs.append(pair)                
                players_tiers = removePlayerFromTierList(pair,mmrs,players_tiers)
                matched[pair[0]] = True
                matched[pair[1]] = True
    return pairs

def removePlayerFromTierList(player_ids, mmrs, players_tiers):
    
    for player_id in player_ids:
        mmr = (mmrs[player_id]//100)*100
        players_tiers[mmr].remove(player_id)
    return players_tiers

def checkGameResult(results, mmrs):
    for result in results:
        winner = result["win"]
        loser  = result["lose"]
        taken  = result["taken"]

        mmrs[winner] += calcMMR(taken)
        mmrs[loser]  += -calcMMR(taken)
    return mmrs

def sol1():
    auth_key = start()
    print(auth_key)

    print(getWaitingLine(auth_key))
    print(getGameResult(auth_key))
    print(getUserInfo(auth_key))

    player_mmrs = [1950 for x in range(player_cnt+1)] 
        
    putMatch(auth_key,[])

    for i in range(594):
        # result 체크해서 mmr 체크하기
        game_results = getGameResult(auth_key)["game_result"]
        player_mmrs = checkGameResult(game_results, player_mmrs)

        # 각 waiting line으로 
        lines = getWaitingLine(auth_key)["waiting_line"]
        waiting_player_tier = setWaitingTier(lines, player_mmrs)

        pairs = setMatching(lines, player_mmrs, waiting_player_tier)
        
        print(putMatch(auth_key,pairs))

    player_with_mmr = []
    for idx, mmr in  enumerate(player_mmrs[1:], start = 1):
        player_with_mmr.append((idx,mmr))

    player_with_mmr.sort(key=lambda x:x[1])
    grades_with_player_id = [{"id":x[0],"grade":idx} for idx,x in enumerate(player_with_mmr)] 

    print(putChangeGrade(auth_key, grades_with_player_id))
    print(putMatch(auth_key,[]))
    print(getScore(auth_key))

    return 1


sol1()