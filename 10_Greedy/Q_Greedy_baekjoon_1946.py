import sys

# 다른 모든 지원자와 비교했을 때
# 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙
# 자신보다 서류 성적이 높은 면접자들의 면접 성적 중 가장 높은 성적보다 A의 성적이 높아야 한다.

# 테스트 케이스 수 : t
t = int(sys.stdin.readline().strip())

for _ in range(t):
    # 지원자 수 : n
    n = int(sys.stdin.readline().strip())  # strip() : 왼쪽, 오른쪽 공백 삭제
    # 지원자 : workers
    workers = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    workers.sort()
    print(workers)

    # 서류 점수 가장 낮은 지원자의 면접 점수 값
    min_rank = workers[0][1]
    cnt = 1
    print(min_rank)

    # 서류 가장 낮은 지원자의 면점 점수보다 다른 지원자가 면접 점수가 낮으면 카운트
    for i in range(n):
        rank = workers[i][1]
        print("rank:{}, min_rank:{}".format(rank, min_rank))
        if rank < min_rank:
            min_rank = rank
            cnt += 1

        print('cnt: ',cnt)
