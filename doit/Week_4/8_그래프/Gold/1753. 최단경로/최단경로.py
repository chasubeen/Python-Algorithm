import sys
input = sys.stdin.readline
from queue import PriorityQueue

## 입력
V, E = map(int, input().split()) # 노드, 에지
K = int(input()) # 출발 노드
distance = [sys.maxsize] * (V+1) # 충분히 큰 수로 초기화
visited = [False] * (V+1) # 방문 여부 저장 리스트
myList = [[] for _ in range(V+1)] # 에지 데이터 저장 인접 리스트
Q = PriorityQueue() # 다익스트라를 위한 우선순위 큐

## 처리
# 인접 리스트에 에지 정보 저장
for _ in range(E):
  u, v, w = map(int, input().split()) # 에지 정보
  myList[u].append((v, w))

# 다익스트라 수행
Q.put((0, K)) # 출발 노드는 우선순위 큐에 넣고 시작
            # 자동으로 거리가 최소인 노드를 선택
distance[K] = 0 # 출발 노드의 값을 0으로 설정

while Q.qsize() > 0:
  current = Q.get()
  c_v = current[1] # 큐의 가장 앞에 있는 에제
  # 방문 여부 확인
  if visited[c_v]:
    continue
  visited[c_v] = True
  
  # 현재 선택 노드의 에지 개수만큼
  for tmp in myList[c_v]:
    next = tmp[0]
    value = tmp[1]

    if distance[next] > distance[c_v] + value:
      distance[next] = distance[c_v] + value # 최소 거리로 업데이트
      # 가중치(거리), 목표 노드 순으로 우선순위 큐 설정
      Q.put((distance[next], next))

## 출력
# 완성된 거리 리스트를 탐색해 출력
for i in range(1, V+1):
  if visited[i]:
    print(distance[i])
  else:
    print("INF")