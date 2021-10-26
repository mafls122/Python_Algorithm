n = 1000 - int(input())
cnt = 0
arr = [500, 100, 50, 10, 5, 1]

for coin in arr:
    cnt += n // coin  # 금액에서 동전금액 몫 : 개수를 cnt에 누적
    n %= coin  # n은 나머지로 초기화

print(cnt)