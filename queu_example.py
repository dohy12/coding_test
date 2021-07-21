from collections import deque

queue = deque()

queue.append(5)
queue.append(3)
queue.append(6)
print(queue.popleft())
queue.append(7)


print(queue)
queue.reverse()
print(queue)