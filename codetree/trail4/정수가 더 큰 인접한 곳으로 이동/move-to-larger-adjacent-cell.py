import sys
input = sys.stdin.readline


## 입력
n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


## 처리
# 상, 하, 좌, 우 (우선순위 순서)
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

x, y = r-1, c-1 # 파이썬 인덱스는 0부터
answer = [grid[x][y]]

while True:
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > grid[x][y]:
            x, y = nx, ny
            answer.append(grid[x][y])
            break
    else: # 네 방향 모두 이동 불가
        break


## 출력
print(*answer)