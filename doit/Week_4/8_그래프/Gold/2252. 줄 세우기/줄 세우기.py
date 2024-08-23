from collections import deque

## 입력
N, M = map(int, input().split())
A = [[] for _ in range(N+1)] # 비교 데이터 저장 인접 리스트
indegree = [0] * (N+1) # 진입 차수 리스트

## 처리
for i in range(M):
  S, E = map(int, input().split()) # 키 비교
  A[S].append(E) # 인접 리스트 데이터 저장
  indegree[E] += 1 # 진입 차수 데이터 저장

queue = deque() # 진입 차수 배열

for i in range(1, N+1):
  if indegree[i] == 0:
    queue.append(i)

# 위상 정렬 수행
while queue:
  now = queue.popleft()
  print(now, end = ' ')
  for next in A[now]:
    indegree[next] -= 1
    if indegree[next] == 0:
      queue.append(next)