"""
Use case of linked lists in queue's and deck's
"""

from collections import deque

# Queue FIFO - fist in first out (imagine a real llife queue)
#   - the newest items go to the tail of the list
#   - 

queue = deque()
queue.append('Mary')
queue.append('John')
queue.append('Mirel')
print(queue)

queue.popleft()
queue.popleft()
print(queue)

# Deck LIFO - last in last out (imagine a browser history)
#   - the newest items go to the head of the list

history = deque()

history.appendleft('first link')
history.appendleft('second link')
history.appendleft('third link')
print(history)

history.popleft()

# history.pop()
# history.pop()
print(history)
