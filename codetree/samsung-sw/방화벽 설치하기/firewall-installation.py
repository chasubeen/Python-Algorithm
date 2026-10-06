## 입력
n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0]*m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split()))) # 맵 그리기


## 처리
# 상/우/하/좌(시계 방향) 이동 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 통해 불이 번지는 것 표현하기
def fire(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 실제로 불이 퍼질 수 있는 경우만 남기기
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 불을 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                fire(nx, ny)

# 현재 맵에서 안전 영역의 크기를 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)를 이용해 방화벽을 설치하면서, 매번 안전 영역의 크기 계산하기
def dfs(count):
    global result
    # 방화벽이 모두(3개) 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 불의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    fire(i, j)
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 방화벽 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1


## 출력
dfs(0)
print(result)