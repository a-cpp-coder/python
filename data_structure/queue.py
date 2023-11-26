# Using List as Queue - still a List, but
# First in First out - FIFO

from collections import deque

a_list = ["Truong", "Quang", "Huy"]
queue = deque(a_list)

queue.append("Quang")
print(queue)

queue.append("Truong")
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)
