from collections import deque

## 입력
# 칸의 크기, 계란 이동 범위(최소 <=  <= 최대)
n, l, r= map(int, input().split())
# 토스트 정보
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


## 처리
# 방향 처리(시계 방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 특정 위치에서 출발해서 데이터 갱신(선 분리)
def process(x, y, idx):
    # (x,y)와 연결된 계란 정보를 담는 리스트
    egg = []
    egg.append((x,y))
    
    # 너비 우선 탐색(BFS)을 위한 큐 자료구조 정의
    q = deque()
    q.append((x, y))
    union[x][y] = idx # 특정 칸 위치 번호
    summary = graph[x][y] # 현재 칸의 계란양
    
    count = 1 # 현재까지 합쳐진 칸 수
    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        # 현재 위치에서 상하좌우 인접 칸을 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인접한 칸을 확인하며
            if 0<=nx<n and 0<=ny<n and union[nx][ny] == -1:
                # 옆에 있는 칸과 계란 양 차이가 L 이상 R 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 칸 합치기(추가)
                    union[nx][ny] = idx
                    summary += graph[nx][ny]
                    count += 1
                    egg.append((nx, ny))
    
    # 합쳐진 칸들끼리 계란물 분배
    for i, j in egg:
        graph[i][j] = summary // count
    return count


## 출력
total_count = 0
# 더 이상 계란물을 분배할 수 없을 때까지 반복
while True:
    union = [[-1]*n for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 칸이 아직 처리되지 않았다면
                process(i, j, idx)
                idx += 1
    # 모든 계란 이동이 끝난 후
    if idx == n*n:
        break
    total_count += 1

# 이동 횟수 출력
print(total_count)