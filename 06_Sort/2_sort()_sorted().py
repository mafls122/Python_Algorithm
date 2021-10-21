# sort() : 원본 리스트를 정렬된 상태로 변환
a_list = [1, 50, 25, 30]
a_list.sort()
print(a_list)  # [1, 25, 30, 50]

# sorted() : 원본 리스트 변경 없이 정렬된 새로운 리스트 반환
# 모든 iterable 객체에 사용 가능
b_list = [5, 10, 99, 24, 30]
c = sorted(b_list)
print(b_list)  # [5, 10, 99, 24, 30]
print(c)  # [5, 10, 24, 30, 99]
