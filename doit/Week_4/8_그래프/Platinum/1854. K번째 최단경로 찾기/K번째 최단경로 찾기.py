import sys
import heapq
input = sys.stdin.readline

## 입력
# 도시(노드) 개수, 도로(에지) 개수, k번째 최단 경로
n, m, k = map(int, input().split()) 
W = [[] for _ in range(n+1)] # 그래프 정보 저장 인접 리스트
# 거리 리스트를 충분히 큰 값으로 초기화
# k개의 row를 갖는 2차원 리스트 형태로 정의
distance = [[sys.maxsize] * k for _ in range(n+1)]

## 처리
for _ in range(m):
  a, b, c = map(int, input().split()) # 시작, 도착, 소요시간
  W[a].append((b,c)) # 인접 리스트에 에지 정보 저장

pq = [(0,1)] # 시작 노드 저장
             # (가중치, 목표 노드) 순서로 저장
distance[1][0] = 0 # 시작 도시 최단 거리 저장
                   # 시작점이기에 0으로 저장

# 다익스트라 수행
while pq:
  # 우선순위 큐에서 데이터 가져오기 -> (거리, 노드)
  cost, node = heapq.heappop(pq)
  # 현재 노드에 연결된 에지 탐색
  for nNode, nCost in W[node]:
    # 새로운 총 거리 = 현재 노드의 거리 + 가중치
    sCost = cost + nCost 
    # 새로운 거리가 더 짧다면
    if distance[nNode][k-1] > sCost:
      # 최단 거리 변경
      distance[nNode][k-1] = sCost
      # 정렬
      distance[nNode].sort()
      # 우선순위 큐에 새로운 데이터 추가(거리, 노드)
      heapq.heappush(pq, [sCost, nNode])

## 출력
# 노드 개수만큼
for i in range(1, n+1):
  # 최초 값(무한대) -> k번째 거리가 x
  if distance[i][k-1] == sys.maxsize:
    print(-1)
  else:
    print(distance[i][k-1])