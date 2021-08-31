# https://programmers.co.kr/learn/courses/30/lessons/42862
# 프로그래머스 코팅테스트 연습 > 탐욕법(Greedy) > 체육복

n = 10
lost = [1, 5, 8, 3, 7]
reserve = [7, 5, 2, 9, 6]

d = {k:1 for k in lost}
reserve.sort()
trash = {}
for i in range(len(reserve)):
    if (d.get(reserve[i],0)==1):
        d.pop(reserve[i])
        trash[reserve[i]] = 1

for i in reserve:
    if (trash.get(i,0)==1):
        continue
    if (d.get(i-1, 0)==1):
        d.pop(i-1)    
    elif (d.get(i+1, 0)==1):
        d.pop(i+1)

print (n - len(d.items()))