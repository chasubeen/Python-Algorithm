from collections import deque

## 변수 초기화
# 상하좌우를 탐색하기 위한 리스트 선언
dx = [-1, 1, 0, 0] # 행 방향 이동
dy = [0, 0, -1, 1] # 열 방향 이동

N, M = map(int, input().split())
A = [[0] * M for _ in range(N)] # 미로판
visited = [[False] * M for _ in range(N)]

## 처리
# 미로판 만들기
for i in range(N):
  numbers = list(input())
  for j in range(M):
    A[i][j] = int(numbers[j])

def BFS(i, j):
  queue = deque()
  queue.append((i, j))
  visited[i][j] = True
  while queue:
    now = queue.popleft()
    # 상하좌우 순서로 방문
    for k in range(4):
      x = now[0] + dx[k]
      y = now[1] + dy[k]
      # 좌표 유효성 검사
      if x >= 0 and y >= 0 and x < N and y < M:
        if A[x][y] != 0 and not visited[x][y]:
          visited[x][y] = True
          A[x][y] = A[now[0]][now[1]] + 1
          queue.append((x, y))

BFS(0, 0)

## 출력
print(A[N-1][M-1])