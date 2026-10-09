from collections import deque
INF =1E9 # 무한을 의미하는 값

## 입력
n = int(input())

# 전체 모든 칸에 대한 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))


## 처리
# 전투 로봇의 현재 레벌, 현재 위치
now_level = 2
now_x, now_y = 0, 0

# 전투 로봇의 초기 시작 위치를 찾은 뒤에 그 위치엔 아무것도 없다고 처리
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 모든 위치까지의 '최단 거리'만 계산
def bfs():
    # 값이 -1이라면 도달할 수 없다는 의미(초기화)
    dist = [[-1]*n for _ in range(n)]
    # 시작 위치는 도달 가능, 그러나 거리가 0
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                # 자신의 레벨보다 작거나 같은 경우에 지나갈 수 있음
                if dist[nx][ny] == -1 and array[nx][ny] <= now_level:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    # 모든 위치까지의 최단 거리 테이블 반환
    return dist

# 최단 거리 테이블이 주어졌을 때, 처리할 몬스터를 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 처리할 수 있는 몬스터일 때
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_level:
                # 가장 가까운 몬스터 1마리만 선택
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]

    if min_dist == INF: # 처리할 수 있는 몬스터가 없는 경우
        return None
    else:
        return x, y, min_dist # 처리할 물고기의 위치와 최단 거리

## 출력
result = 0 # 최종 답안
killed = 0 # 현재 레벨에서 처리한 양

while True:
    # 처리할 수 있는 몬스터의 위치 찾기
    value = find(bfs())
    # 처리할 수 있는 몬스터가 없는 경우, 현재까지 움직인 거리를 출력
    if value == None:
        print(result)
        break
    else:
        # 현재 위치 갱신 및 이동 거리 변경
        now_x, now_y = value[0], value[1]
        result += value[2]

        # 몬스터를 처리한 위치에는 이제 아무것도 없도록 처리
        array[now_x][now_y] = 0
        killed += 1
        # 자신의 현재 크기 이상으로 처리한 경우, 레벨업
        if killed >= now_level:
            now_level += 1
            killed = 0