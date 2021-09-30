import requests
import json 

user_key = "tester"

host = "http://127.0.0.1:8000"

# # GET 
# res = requests.get('http://127.0.0.1:5000') 
# print(str(res.status_code) + " | " + res.text) 

# POST (JSON)
#headers = {'Content-Type': 'application/json; chearset=utf-8'} 
#data = {'user_key':user_key,'problem_id':0,'number_of_elevators':1} 
res = requests.post(host + '/start' + '/' + user_key + '/'+str(1)+'/'+str(1))
data = json.loads(res.text)

token = data['token']
elevator = data['elevators'][0]

res = json.loads(requests.get(host + '/oncalls', headers={'X-Auth-Token': token}).text)

call_info = {}
call_list = []

calls = res['calls']
for c in calls:
    if c["id"] not in call_info:
        call_info[c["id"]] = {"start":c["start"], "end":c["end"]}
        call_list.append(c["id"])

print(call_info)

data = {"commands":[{'elevator_id':0, 'command':'UP'}]}
header = {'Content-Type': 'application/json', 'X-Auth-Token': token}
res = requests.post(host + '/action', json=data , headers=header).json()
res = requests.post(host + '/action', json=data , headers=header).json()
res = requests.post(host + '/action', json=data , headers=header).json()
res = requests.post(host + '/action', json=data , headers=header).json()

res = json.loads(requests.get(host + '/oncalls', headers={'X-Auth-Token': token}).text)
print(res)
# tmp = json.loads(res.text)
# print() # status_code
