from collections import deque

q = deque(["일번", "이번", "삼번"])
print(q)  # deque(['일번', '이번', '삼번'])

q.append("사번")
print(q)  # deque(['일번', '이번', '삼번', '사번'])

q.popleft()
print(q)  # deque(['이번', '삼번', '사번'])

q.pop()
print(q)  # deque(['이번', '삼번'])

q.appendleft("영번")
print(q)  # deque(['영번', '이번', '삼번'])