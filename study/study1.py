# https://programmers.co.kr/learn/courses/30/lessons/43238
# 코딩테스트 연습 > 이분탐색> 입국심사

def solution(n, times):
    return  binarySearch(times[0], times[0]*n,times, n, False)

def binarySearch(left, right, times, n, maxRight):
    if left>right:
        return maxRight

    mid = int((left + right)/2)    

    cnt = 0
    for time in times:
        cnt += int(mid/time)
    
    if cnt<n:
        return binarySearch(mid+1, right, times, n , mid+1)
    else :
        return binarySearch(left, mid-1, times, n , mid)   

n = 6
times = [1, 6]

print(solution(n, times))