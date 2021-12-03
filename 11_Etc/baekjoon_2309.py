# 9개의 난쟁이 키 데이터 추가
h = []
for i in range(9):
    h.append(int(input()))

# 모든 키의 합에서 i와 j(임의의 2개 값)를 뺀 값이 100이면 리스트에서 지워준다.
for i in h:
    for j in h[1:]:
        if sum(h) - i - j == 100:
            h.remove(i)
            h.remove(j)

h.sort()
for i in h:
    print(i)