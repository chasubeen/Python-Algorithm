## 입력
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


## 처리
dx = [-1, 0, 1, 0]  # 상 우 하 좌
dy = [0, 1, 0, -1]

def simulate(x, y, d):
    t = 1  # 격자 안으로 들어오는 시간
    while 0 <= x < n and 0 <= y < n:
        if grid[x][y] == 1:    # '/'
            d ^= 1
        elif grid[x][y] == 2:  # '\'
            d = 3 - d
        x += dx[d]
        y += dy[d]
        t += 1
    return t

ans = 0
for i in range(n):
    ans = max(ans,
              simulate(0, i, 2),      # 위에서 아래로
              simulate(n - 1, i, 0),  # 아래에서 위로
              simulate(i, 0, 1),      # 왼쪽에서 오른쪽으로
              simulate(i, n - 1, 3))  # 오른쪽에서 왼쪽으로


## 출력
print(ans)