class Queue(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    # 정렬 바꾸기
    def _transfer(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    # 큐 뒤쪽에 항목 삽입
    def enqueue(self, item):
        return self.in_stack.append(item)

    # 큐 앞쪽의 항목 반환 및 제거
    def dequeue(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack.pop()
        else:
            print("Queye is empty!")

    # 큐 크기 확인
    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    # 큐 앞 항목 조회
    def peek(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return self.out_stack[-1]
        else:
            print("Queue is empty!")

    def __repr__(self):
        if not self.out_stack:
            self._transfer()
        if self.out_stack:
            return repr(self.out_stack)
        else:
            print("Queue is empty")

    def isEmpty(self):
        return not (bool(self.in_stack) or bool(self.out_stack))

if __name__ == '__main__':
    queue = Queue()
    print("큐에 숫자 0~9를 추가")
    for i in range(10):
        queue.enqueue(i)
    print("큐 크기 : {}".format(queue.size()))
    print(queue)
    print("큐 peek : {}".format(queue.peek()))
    print("큐 deqeue : {}".format(queue.dequeue()))
    print("큐 peek : {}".format(queue.peek()))
    print("큐가 비어있는가? : {}".format(queue.isEmpty()))
    print(queue)