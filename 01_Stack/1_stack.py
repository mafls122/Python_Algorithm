stack_list = []

stack_list.append(1)
stack_list.append(2)
stack_list.append(3)
stack_list.pop()
stack_list.append(4)
stack_list.append(5)
stack_list.append(6)
stack_list.pop()

print(stack_list)  # [1, 2, 4, 5]

'''
stack 은
append() 후입
pop() 선출
을 통해 쉽게 구현 가능
'''



