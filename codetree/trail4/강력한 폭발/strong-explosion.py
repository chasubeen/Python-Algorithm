## 입력
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

bombs = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bombs.append((i, j))

m = len(bombs)


## 처리
# 폭탄이 없애는 칸 방향
directions = [
    [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)], # 세로
    [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)], # 십자
    [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, 0)] # x자
]

visited = [[0] * n for _ in range(n)]
answer = 0


def apply_bomb(r, c, bomb_type, delta):
    for dr, dc in directions[bomb_type]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < n and 0 <= nc < n:
            visited[nr][nc] += delta


def backtrack(depth):
    global answer

    # 모든 폭탄의 종류를 선택한 경우
    if depth == m:
        count = 0

        for i in range(n):
            for j in range(n):
                if visited[i][j] > 0:
                    count += 1

        answer = max(answer, count)
        return

    r, c = bombs[depth]

    # 현재 폭탄에 대해 3가지 종류 탐색
    for bomb_type in range(3):
        # 폭탄 배치
        apply_bomb(r, c, bomb_type, 1)

        # 다음 폭탄 탐색
        backtrack(depth + 1)

        # 폭탄 제거 (원상복구)
        apply_bomb(r, c, bomb_type, -1)

backtrack(0)


## 출력
print(answer)