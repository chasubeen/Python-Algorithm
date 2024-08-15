import sys
from collections import deque
input = sys.stdin.readline

## 입력
# 노드 개수, 에지 개수, 목표 거리, 시작점
N, M, K, X = map(int, input().split())
A = [[] for _ in range(N+1)] # 그래프 데이터 저장 인접 리스트
answer = [] # 정답 리스트
visited = [-1] * (N+1) # 방문 리스트(-1로 초기화)

## 처리
def BFS(v):
  queue = deque()
  queue.append(v) # queue 자료구조에 시작 노드 삽입
  visited[v] += 1 # 거리 저장 형태로 1 증가
  
  # 큐가 빌 때까지
  while queue:
    # 큐에서 노드 데이터 가져오기
    now_node = queue.popleft()
    for i in A[now_node]:
      # 현재 노드의 연결 노드 중 미방문 노드라면
      if visited[i] == -1:
        visited[i] = visited[now_node] + 1 # visited 1 증가
        queue.append(i) # 큐에 노드 삽입

for _ in range(M):
  S, E = map(int, input().split())
  # A 인접 리스트에 그래프 데이터 저장
  A[S].append(E)

BFS(X)

for i in range(N+1):
  # 방문 거리가 K인 노드의 숫자를 정답 리스트에 더하기
  if visited[i] == K:
    answer.append(i)
    
## 출력
if not answer:
  print(-1)
else:
  answer.sort() # 정답 데이터 오름차순 정렬
  # 순차 출력
  for i in answer:
    print(i)