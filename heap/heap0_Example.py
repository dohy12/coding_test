import heapq # heapq import

heap = [] # 새 heap을 리스트로 선언

# 힙에 원소 추가 O(logN)
heapq.heappush(heap, 2)
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)

print(heap)

# 힙에서 원소 삭제
print(heapq.heappop(heap))
print(heap)

# 힙에서 최솟값 삭제 안하고 받아오기
print(heap[0]) # 주의할점 ) heap[1]한다고 두번째로 작은 원소는 못받아온다.

# 기존 리스트를 힙으로 변환  O(N)
l = [4,1,7,3,8,5]
heapq.heapify(l)
print(l)

# 최대힙? 튜플을 응용한다
nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
    heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
    print(heapq.heappop(heap)[1]) 


