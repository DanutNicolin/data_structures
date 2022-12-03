"""
Use case of linked lists in queue's and deck's
"""

from collections import deque

# Queue FIFO - fist in first out (imagine a real llife queue)
queue = deque()
queue.append('Mary')
queue.append('John')
queue.append('Mirel')
print(queue)

queue.popleft()
queue.popleft()
print(queue)

# Deck LILO - last in last out (imagine a browser history)
history = deque()

history.appendleft('first link')
history.appendleft('second link')
history.appendleft('third link')
print(history)

history.pop()
history.pop()
print(history)
