# 아무것도 안했을때
import requests

x_auth_token = "7d9bde98a7632ed292eb1cb1ca509e0b"
host = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"

def start():
    res  = requests.post(host+"/start", headers={"X-Auth-Token":x_auth_token}, json={"problem":2}).json()
    return res["auth_key"]

def putSimpulate(auth_key):
    res = requests.put(host+"/simulate",headers={"Authorization":auth_key}, json={"commands":[]}).json()
    print("time:",res["time"])
    return res["status"]

def getScore(auth_key):
    return requests.get(host+"/score",headers={'Authorization':auth_key}).json()

def sol1():
    auth_key = start()

    while True:
        if putSimpulate(auth_key)=="finished":
            print(getScore(auth_key))
            break


sol1()