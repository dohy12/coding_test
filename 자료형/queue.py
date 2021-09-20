# 일반 queue는 list를 사용해서 만들 수 있다
queue = [4,5,6]
queue.append(7)
queue.append(8)
print(queue)

print(queue.pop(0)) # 성능이 dequeue에 비해서 좋지 않다.
print(queue.pop())  # 맨 뒤에꺼가 날아감

print(queue)

from collections import deque

dq = deque([4,5,6])
dq.append(7)
dq.append(8)

print(dq)
print(dq.popleft(),dq.popleft())  # list의 pop(0)보다 성능이 훨씬 좋다
print(dq)

dq.appendleft(3)  # list의 insert(0, x)보다 월등히 성능이 좋다
dq.appendleft(2)
print(dq)

dq += [2,3,4,5]
print(dq[:3])