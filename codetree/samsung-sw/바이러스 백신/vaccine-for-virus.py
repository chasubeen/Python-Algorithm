import sys
from collections import deque
from itertools import combinations


## 입력
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


## 처리
hospitals = []
virus_count = 0

for r in range(N) :
    for c in range(N):
        if board[r][c] == 2:
            hospitals.append((r,c))
        elif board[r][c] == 0:
            virus_count += 1

# 애초에 제거할 바이러스가 없는 경우
if virus_count == 0:
    print(0)
    sys.exit()

INF = 10**9
answer = INF

# 상/하/좌/우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(active_hospitals):
    # -1 : 아직 백신이 도달하지 않음
    dist = [[-1] * N for _ in range(N)]

    q = deque()

    # 선택한 M개의 병원에서 동시에 시작(Brute-force)
    for r, c in active_hospitals:
        dist[r][c] = 0
        q.append((r, c))

    remain = virus_count
    elapsed = 0

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 범위 밖
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 벽
            if board[nr][nc] == 1:
                continue

            # 이미 방문
            if dist[nr][nc] != -1:
                continue

            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

            # 바이러스가 있는 칸에 도착
            if board[nr][nc] == 0:
                remain -= 1
                elapsed = max(elapsed, dist[nr][nc])

                # 모든 바이러스 제거 완료
                if remain == 0:
                    return elapsed

    # BFS가 끝났는데 바이러스가 남아 있음
    return INF


# 병원들 중 M개를 고르는 모든 경우 확인
for active_hospitals in combinations(hospitals, M):
    cur_time = bfs(active_hospitals)
    answer = min(answer, cur_time)


## 출력
if answer == INF:
    print(-1)
else:
    print(answer)