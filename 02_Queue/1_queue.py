from collections import deque

q_list = deque()

q_list.append(1)
q_list.append(2)
q_list.append(3)
q_list.popleft()
q_list.append(4)
q_list.append(5)
q_list.append(6)
q_list.popleft()

print(q_list)  # deque([3, 4, 5, 6])

'''
queue
append() 선입
pop() 선출
을 통해 쉽게 구현 가능
'''