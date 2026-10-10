import sys
from collections import deque
input = sys.stdin.readline

## 입력
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


## 처리
dist = [[-1]*n for _ in range(n)]
q = deque()
# 상한 귤 K개를 전부 시작점으로 -> BFS
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            dist[i][j] = 0
            q.append((i, j))

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))


## 출력
for i in range(n):
    row = []
    for j in range(n):
        # 처음부터 비어있던 칸
        if grid[i][j] == 0:
            row.append(-1)
        # 영원히 방문 x -> 상하지 않음
        elif dist[i][j] == -1:
            row.append(-2)
        else:
            row.append(dist[i][j])
    
    print(*row)