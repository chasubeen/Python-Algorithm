import sys
from collections import deque
input = sys.stdin.readline

## 입력
N = int(input())  # 노드의 개수
tree = [[] for _ in range(N + 1)]  # 트리 데이터 저장

# 인접 리스트에 트리 데이터 저장
for _ in range(N - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

depth = [0] * (N + 1)  # 노드 깊이 리스트
# 노드 조상 리스트 (최대 2^16까지 필요)
parent = [[0] * 17 for _ in range(N + 1)]  
visited = [False] * (N + 1)  # 방문 여부 저장 리스트

## 처리
def BFS(node):
    queue = deque([node])
    visited[node] = True  # 현재 노드 방문 기록

    while queue:
        now_node = queue.popleft()  # deque로 popleft() 사용

        for next_node in tree[now_node]:
            if not visited[next_node]:
                visited[next_node] = True  # 방문 기록 저장
                parent[next_node][0] = now_node  # 바로 위 부모 노드 저장
                depth[next_node] = depth[now_node] + 1  # 현재 깊이 저장
                queue.append(next_node)

BFS(1)  # BFS를 통해 depth와 부모 노드 구하기

# 각 노드의 2^i 번째 부모 노드 기록(Sparse Table 방식)
for i in range(1, 17):
    for j in range(1, N + 1):
        parent[j][i] = parent[parent[j][i - 1]][i - 1]

# LCA 함수
def executeLCA(a, b):
    if depth[a] < depth[b]:
        a, b = b, a  # 깊이를 맞추기 위해 swap

    # 깊이 맞추기
    for i in range(16, -1, -1):
        if depth[a] - depth[b] >= (1 << i):
            a = parent[a][i]

    if a == b:
        return a

    # 공통 조상 찾기
    for i in range(16, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

## 출력
M = int(input())
mydict = dict()
for _ in range(M):
    a, b = map(int, input().split())
    # 같은 질문일 경우 재계산을 하지 않기 위해 딕셔너리 자료형 사용
    if not mydict.get((a, b), 0):
        mydict[(a, b)] = mydict[(b, a)] = executeLCA(a, b)
    print(mydict.get((a, b)))