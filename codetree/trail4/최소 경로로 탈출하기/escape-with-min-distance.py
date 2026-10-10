import sys
from collections import deque
input = sys.stdin.readline


## 입력
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


## 처리
dist = [[-1]*m for _ in range(n)]
dist[0][0] = 0
q = deque([(0, 0)])

while q:
    x, y = q.popleft()
    for dx, dy in ((-1, 0), (1,0), (0,-1), (0,1)):
        nx, ny = x + dx, y + dy
        # 방문 가능한 경우
        if 0<= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))


## 출력
print(dist[n-1][m-1])