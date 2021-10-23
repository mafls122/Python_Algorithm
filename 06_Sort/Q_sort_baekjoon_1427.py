n = input()
a = []
res = ''
for i in n:
    a.append(int(i))
a = sorted(a, reverse=True)
for i in a:
    res += str(i)
print(res)


# 다른 방법
arr = input()
# i : 9 ~ 0, j가 입력된 수 배열
for i in range(9, -1, -1):
    for j in arr:
        # arr를 하나씩 가져와서 ex)9~0 이면 출력
        if int(j) == i:
            print(i, end='')