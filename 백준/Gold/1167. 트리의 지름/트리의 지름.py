from collections import deque

## 입력
N = int(input()) # 노드 개수
A = [[] for _ in range(N+1)] # 인접 리스트

# 인접 리스트에 그래프 구조 저장
# 노드 및 거리를 튜플 형태로 저장
for _ in range(N):
  Data = list(map(int, input().split()))
  index = 0
  S = Data[index] # 시작
  index += 1
  while True:
    E = Data[index] # 정점(노드)
    if E == -1: # 끝이라면
      break
    V = Data[index + 1] # 에지(가중치)

    A[S].append((E, V))
    index += 2

distance = [0] * (N+1) # 거리 리스트 초기화
visited = [False] * (N+1) # 방문 리스트 초기화

## 처리
# BFS 구현
def BFS(v):
  queue = deque()
  queue.append(v)
  visited[v] = True

  while queue:
    now_Node = queue.popleft()
    for i in A[now_Node]:
      if not visited[i[0]]:
        visited[i[0]] = True
        queue.append(i[0])
        distance[i[0]] = distance[now_Node] + i[1] 

BFS(1)

# 최대 거리 찾기
Max = 1
for i in range(2, N+1):
  if distance[Max] < distance[i]:
    Max = i # 거리 리스트 값 중 Max 값으로 시작점 재설정

# 변수 초기화
distance = [0] * (N+1)
visited = [False] * (N+1)
BFS(Max)

## 출력
# 최대 거리 출력
distance.sort()
print(distance[N])