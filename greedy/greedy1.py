# https://programmers.co.kr/learn/courses/30/lessons/42862
# 프로그래머스 코팅테스트 연습 > 탐욕법(Greedy) > 체육복

n = 10
lost = [1, 5, 8, 3, 7]
reserve = [7, 5, 2, 9, 6]

l = [1] * n

for i in lost:
    l[i] -= 1
    
for i in reserve:
    l[i] += 1
    
if (l[0]==2 and l[1] == 0) or (l[0]==0 and l[1] == 2):
    l[0] = l[1] = 1

for i in range(1,n-1):
    if l[i]==0 and l[i-1]==2:
        l[i] = l[i-1] = 1        
    if l[i]==0 and l[i+1]==2:
        l[i] = l[i+1] = 1  
    
if (l[n-1]==2 and l[n-2]==0) or (l[n-1]==0 and l[n-2]==2):
    l[n-1] = l[n-2] = 1
        
answer = 0
for i in range(n):
    if(l[i]>0):
        answer += 1  
print(answer)