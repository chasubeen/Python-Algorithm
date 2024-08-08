from collections import deque

## 입력
N, M, start = map(int, input().split())
A = [[] for _ in range(N+1)] # 인접 리스트

# 노드들 간의 연결 정보 저장
for _ in range(M):
  s, e = map(int, input().split())
  # 양방향 에지이므로 양쪽에 에지를 더해줌
  A[s].append(e)
  A[e].append(s)


## 처리
# 인집 리스트를 오름차순으로 정렬
for i in range(N+1):
  A[i].sort()

# === DFS: LIFO ===
def DFS(v):
  print(v, end = ' ')
  visited[v] = True
  for i in A[v]:
    if not visited[i]:
      DFS(i)  
      
visited = [False] * (N+1) # 방문 리스트 초기화
DFS(start) # DFS 시작

# === BFS: FIFO ===
def BFS(v):
  queue = deque() # 큐 자료구조 선언
  queue.append(v) # 시작 노드 삽입
  visited[v] = True # 현재 노드 방문 기록 저장
  # 큐에 요소가 있을 때까지(빌 때까지)
  while queue:
    # 큐에서 노드 데이터 가져오기
    now_node = queue.popleft() 
    # 가져온 노드 출력
    print(now_node, end = ' ') 
    # 현재 노드의 연결 노드 중 미방문 노드를 큐에 삽입(append)하고 
    # 방문 리스트에 기록
    for i in A[now_node]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)

print() # 줄바꿈
visited = [False] * (N+1) # 방문 리스트 초기화
BFS(start) # BFS 시작