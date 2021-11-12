# 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고,
# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수
# 회의의 시작시간과 끝나는 시간이 같을 수도 있다.
# 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

import sys

def meet(n):
    lst = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    # 시작 시간순으로 오름차순 정렬
    lst = sorted(lst, key=lambda x: x[0])
    # 끝나는 시간순으로 오름차순 정렬
    lst = sorted(lst, key=lambda x: x[1])
    print(lst) # [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

    cnt = 0
    # 끝나는 시간
    end_time = 0
    # 끝나는 시간이 크거나 같다면 카운트
    for i, j in lst:
        if i >= end_time:
            end_time = j
            cnt += 1
    return cnt

if __name__ == '__main__':
    # 사용하고자 하는 회의실 수 mn
    mn = int(input())
    print(meet(mn))