
class Stack(object):
    def __init__(self):
        self.items = []

    # 스택 비어있는지 확인
    def isEmpty(self):
        return not bool(self.items)

    # 스택 후입
    def push(self,value):
        self.items.append(value)

    # 스택 선출
    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Stack is empty.")

    # 스택 크기
    def size(self):
        return len(self.items)

    # 스택 마지막 항목 조회
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Stack is empty")

    def __repr__(self):
        return repr(self.items)

if __name__ == '__main__':
    stack = Stack()
    print("스택에 0~9까지 숫자 추가")
    for i in range(10):
        stack.push(i)
    print("스택 크기 : {}".format(stack.size()))
    print(stack)
    print("스택 peek : {}".format(stack.peek()))
    print("스택 pop : {}".format(stack.pop()))
    print("스택이 비어있는가? : {}".format(stack.isEmpty()))
    print(stack)