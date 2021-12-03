def findPrimes(num):
    # 리스트 초기화 : 0,1 자리는 False로 초기화, 2~100까지 True로 시작한다.
    sieve = [False, False] + ([True] * (num - 1))
    res = []

    # 2부터 자신의 수까지
    for i in range(2, num + 1):
        if sieve[i]:  # True(소수)일 경우 카운트
            res.append(i)
        for j in range(i * 2, num + 1, i):  # ex) 2의 배수 리스트는 False로 변경 4,6,8,,,
            sieve[j] = False
    print(sieve)
    print(len(sieve))
    print(res)
    return res

# 거의 소수 카운트
def count_prime(s, e):
    cnt = 0
    # 리스트 초기화
    plist = findPrimes(e)
    # print(plist)

    for i in plist:
        for j in range(2, 10**14):
            n = i ** j
            if s <= n and n <= e :
                cnt += 1
            elif n > e :
                break
    return cnt

# 범위 a <= 소수 <= b
a, b = map(int, input().split())
print(count_prime(a, b))