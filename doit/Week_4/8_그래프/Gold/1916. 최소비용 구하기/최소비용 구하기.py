import sys
input = sys.stdin.readline
from queue import PriorityQueue

## 입력
N = int(input()) # 도시 개수
M = int(input()) # 버스 개수
myList = [[] for _ in range(N+1)] # 에지 데이터 저장 인접 리스트
dist = [sys.maxsize] * (N+1) # 충분히 큰 수로 초기화
visit = [False] * (N+1) # 방문 여부 저장 리스트

# 인접 리스트에 에지 정보 저장
for _ in range(M):
  start, end, weight = map(int, input().split()) # 에지 정보
  myList[start].append((end, weight))

start_idx, end_idx = map(int, input().split()) # 출발, 도착


## 처리
# 다익스트라 함수 구현
def dijkstra(start, end):
  pq = PriorityQueue()
  # 출발 노드를 우선순위 큐에 넣고 시작
  pq.put((0, start)) # 거리, 도시

  dist[start] = 0
  while pq.qsize() > 0:
    nowNode = pq.get()
    now = nowNode[1] # 큐의 가장 앞에 있는 에제
    # 방문 여부 확인
    if not visit[now]:
      visit[now] = True
      # 현재 선택 노드의 에지 개수만큼
      for n in myList[now]:
        if not visit[n[0]] and dist[n[0]] > dist[now] + n[1]:
          # 최소 거리로 업데이트
          dist[n[0]]= dist[now] + n[1]
          # 가중치(거리), 목표 노드 순으로 우선순위 큐 설정
          pq.put((dist[n[0]], n[0]))
          
  return dist[end]

## 출력
print(dijkstra(start_idx, end_idx))