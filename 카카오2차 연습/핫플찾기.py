import requests

x_auth_token = "c258e6b398b0ea36be57045c1250ed6a"

res = [[] for x in range(3)]
res[0] = requests.get("https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-1.json").json()
res[1] = requests.get("https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-2.json").json()
res[2] = requests.get("https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-3.json").json()

block = [[0,0] for x in range(60*60)]

for idx in range(3):
    for calls in res[idx].values():
        for call in calls: #[0]대여 [1]반납 [2]시간
            block[call[0]][0] +=1
            block[call[1]][1] +=1



print("대여")
for i in range(60):
    st = ""
    for j in range(60):
        st += str(block[j*60+(59-i)][0]) + " "
    print(st)

print("-------------------------------------")
print("반납")

for i in range(60):
    st = ""
    for j in range(60):
        st += str(block[j*60+(59-i)][1]) + " "
    print(st)



