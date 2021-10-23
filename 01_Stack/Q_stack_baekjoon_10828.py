import sys

n = int(input())
stack = []

def push(n):
    return stack.append(n)

def pop(sta):
    if sta:
        return sta.pop()
    else:
        return -1

def size(sta):
    return len(sta)

def empty(sta):
    if sta:
        return 0
    else:
        return 1

def top(sta):
    if sta:
        return sta[-1]
    else:
        return -1

for _ in range(n):
    data = sys.stdin.readline().split()
    if data[0] == "push":
        push(data[1])
    elif data[0] == "pop":
        print(pop(stack))
    elif data[0] == "size":
        print(size(stack))
    elif data[0] == "empty":
        print(empty(stack))
    elif data[0] == "top":
        print(top(stack))