import sys
input = sys.stdin.readline

## 입력
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize]*(N+1) # 적당히 큰 수로 초기화

for i in range(M):
  S, E, W = map(int, input().split()) # 출발, 도착, 시간
  edges.append((S,E,W)) # 튜플 형태로 저장

## 처리
# 1. 리스트 초기화
distance[1] = 0
# 2. 정답 리스트 업데이트
for _ in range(N-1):
  for S, E, W in edges:
    if distance[S] != sys.maxsize and distance[E] > distance[S] + W:
      distance[E] = distance[S] + W
# 3. 음수 사이클 확인
minus = False
for S, E, W in edges:
  # 갱신되는 경우가 생긴다면
  if distance[S] != sys.maxsize and distance[E] > distance[S] + W:
    minus = True

## 처리
# 음수 사이클 존재 x
if not minus:
  for i in range(2, N+1):
    # 단, 거리 리스트의 값이 무한대이면(방문 x) -1 출력
    if distance[i] != sys.maxsize:
      print(distance[i])
    else:
      print(-1)
# 음수 사이클 존재
else:
  print(-1)