memo = {}  # 메모이제이션
def fib(n):
    # 기록되어 있으면 바로 return
    if n in memo:
        return memo[n]

    if n < 2:
        memo[n] = 1
        return 1
    else:
        memo[n] =  fib(n-1) + fib(n-2)
        # print(memo)
        return memo[n]

if __name__ == '__main__':
    # 피보나치수열이란 1,2항은 1이며 그 뒤 모든 항은 바로 앞 두항의 합인 수열
    # ex) memo = {1: 1, 0: 1, 2: 2, 3: 3, 4: 5, 5: 8, 6: 13, 7: 21, 8: 34, 9: 55, 10: 89}
    print(fib(10))  # 89

