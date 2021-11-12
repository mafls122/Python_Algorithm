# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는가

from collections import deque

def bfs(x, y, target_x, target_y):
    # 나이트가 이동할 수 있는 칸 : 8개
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    # 현재 위치와 이동하고자 하는 위치가 같으면 0 리턴
    if x == target_x and y == target_y:
        return 0

    q = deque()
    q.append((x, y, 0))  # (x좌표, y좌표, 이동한 횟수)

    while q:
        x, y, cnt = q.popleft()
        for i in range(8):
            # 이동한 칸 : nx, ny
            nx, ny = x + dx[i], y + dy[i]
            # 이동한 곳이 처음간 곳이면 1 표시
            if 0 <= nx < l and 0 <= ny < l and chess[nx][ny] == 0:
                chess[nx][ny] = 1
                # 목표 위치인 경우 횟수 출력
                if nx == target_x and ny == target_y:
                    return cnt + 1
                else:
                    q.append((nx, ny, cnt+1))

if __name__ == '__main__':
    # 테스트 케이스 수 : t
    t = int(input())

    for _ in range(t):
        # 체스판 한 변의 길이 : l
        l = int(input())
        # chess 리스트 초기화 : chess (l x l)
        chess = [[0]*l for _ in range(l)]
        # 현재 있는 칸 : x, y
        x, y = map(int, input().split())
        # 이동 표시
        chess[x][y] = 1
        # 이동하려는 칸 : target_x, target_y
        target_x, target_y = map(int, input().split())
        print(bfs(x, y, target_x, target_y))