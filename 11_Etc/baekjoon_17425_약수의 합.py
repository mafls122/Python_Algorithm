# 내가 짠 시간초과 코드
# n = int(input())
# res = []
# snum = 0
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if i % j == 0:
#             res.append(j)
#     snum += sum(list(set(res)))
#     res.clear()
            
# print(snum)

# 간단 코드
n = int(input())

for _ in range(n):
    num = int(input())
    res = 0
    for i in range(1,num+1):
        res += (num//i)*i
        print(res, num, i)
    print(res)