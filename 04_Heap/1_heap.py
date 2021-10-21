import heapq

a_list = [11, 7, 3, 4]
# heapq.heapify(list) : 리스트를 힙으로 변환
heapq.heapify(a_list)
print(a_list)

b_list = []
# heapq.heappush(heap, item) : 힙에 항목 삽입
heapq.heappush(b_list, (20, "z"))
heapq.heappush(b_list, (2, "b"))
heapq.heappush(b_list, (5, "h"))
print(b_list)

# heapq.heappop(heap) : 힙에서 가장 작은 항목 제거 후 반환
heapq.heappop(a_list)
print(a_list)

heapq.heappop(b_list)
print(b_list)

