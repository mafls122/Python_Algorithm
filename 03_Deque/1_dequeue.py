from collections import deque

q = deque(["일번", "이번", "삼번"])
print(q)

q.append("사번")
print(q)

q.popleft()
print(q)

q.pop()
print(q)

q.appendleft("영번")
print(q)