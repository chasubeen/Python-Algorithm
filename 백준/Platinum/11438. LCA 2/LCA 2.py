import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

## 입력
N = int(input()) # 수의 개수
tree = [[0] for _ in range(N + 1)] # 트리 데이터 저장

# 인접 리스트에 트리 데이터 저장
for _ in range(0, N - 1):  
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

depth = [0] * (N + 1) # 노드 깊이 리스트
visited = [False] * (N + 1) # 방문 여부 저장 리스트
temp = 1
kmax = 0 # 최대 가능 높이


## 처리
# 최대 가능 depth 구하기
while temp <= N:  
    temp <<= 1
    kmax += 1

# 노드 조상 리스트
parent = [[0 for j in range(N + 1)] for i in range(kmax + 1)]

# BFS 함수 구현
def BFS(node):
    queue = deque()
    queue.append(node) # 출발 노드 넣기
    visited[node] = True # 현재 노드 방문 기록 업데이트
    
    level = 1 # 트리 깊이
    now_size = 1 # 현재 깊이에서의 트리 크기
    count = 0 # 카운트
    
    while queue:
        now_node = queue.popleft()
        # 현재 노드와 연결된 노드 탐색
        for next in tree[now_node]:
            # 미 방문 노드라면
            if not visited[next]:
                visited[next] = True # 방문 기록 업데이트
                queue.append(next) # 큐에 데이터 삽입
                parent[0][next] = now_node  # 부모 노드 저장
                depth[next] = level  # 노드 depth 저장
        count += 1

        # 현재 깊이의 모든 노드 방문하기
        if count == now_size:
            count = 0
            now_size = len(queue)
            level += 1


BFS(1)

for k in range(1, kmax + 1):
    for n in range(1, N + 1):
        parent[k][n] = parent[k - 1][parent[k - 1][n]]

def excuteLCA(a, b):
    if depth[a] > depth[b]:  # 더 깊은 depth가 b가 되도록
        temp = a
        a = b
        b = temp

    for k in range(kmax, -1, -1):  # depth 빠르게 맞추기
        if pow(2, k) <= depth[b] - depth[a]:
            if depth[a] <= depth[parent[k][b]]:
                b = parent[k][b]

    for k in range(kmax, -1, -1):  # 조상 빠르게 찾기
        if a == b: break
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    LCA = a
    if a != b:
        LCA = parent[0][LCA]
    return LCA

## 출력
M = int(input()) # 질의 개수
for _ in range(M):
    a, b = map(int, input().split())
    print(str(excuteLCA(a, b)))
    print("\n")