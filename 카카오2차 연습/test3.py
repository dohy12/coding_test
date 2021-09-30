import requests

host = "127.0.0.1:8000"

token = "token"

def p0_simnulator():

    res = requests.post(host + "/start", headers={"X-Auth-Token":token}, json={"problem":1}).json()
    auth_key = res["auth_key"]


    



