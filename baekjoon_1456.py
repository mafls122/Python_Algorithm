# 어떤 수가 소수의 N제곱(N ≥ 2) 꼴일 때, 그 수를 거의 소수라고 한다.
# 두 정수 A와 B가 주어지면, A보다 크거나 같고, B보다 작거나 같은 거의 소수가 몇 개인지 출력한다.

# 소수 판별
def isPrime(n):
    for i in range(2, n):
        # 2부터 n-1까지 나누어 떨어지는 수가 있다면 소수가 아님
        if n % i == 0:
            return False
    return True

# 거의 소수 카운트
def count_prime(s, e):
    cnt = 0

    # 리스트 초기화
    plist = []
    for i in range(s, e+1):
        plist.append(False)

    # s부터 e까지 소수인 경우 거의 소수에 True로 변경
    for i in range(s, e+1):
        if isPrime(i):
            prime = i
            for j in range(prime**i, e+1):
                plist[j] = True
    for i in plist:
        if i:
            cnt += 1
    return cnt

# 범위 a <= 소수 <= b
a, b = map(int, input().split())
print(count_prime(a, b))
