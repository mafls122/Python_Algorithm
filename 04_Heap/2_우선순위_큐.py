# 우선순위가 높은 데이터부터 출력
import heapq

def heap_sort(iterable):
    heap = []
    res = []
    # iterable을 힙에 삽입
    for i in iterable:
        heapq.heappush(heap, i)
    # 힙에서 정리된 원소를 res에 차례대로 삽입
    for i in range(len(heap)):
        res.append(heapq.heappop(heap))

    return res

if __name__ == '__main__':
    arr = [10, 20, 30, 40, 5, 8, 99]

    res = heap_sort(arr)
    print(res)  # [5, 8, 10, 20, 30, 40, 99]