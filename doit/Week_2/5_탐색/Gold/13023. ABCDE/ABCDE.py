import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

## 입력
N, M = map(int, input().split())
arrive = False
A = [[] for _ in range(N+1)] # 인접 리스트
visited = [False] * (N+1)

# 인접 리스트(친구 관계) update
for _ in range(M):
  s, e = map(int, input().split())
  A[s].append(e)
  A[e].append(s)

## 처리
# DFS 구현
def DFS(now, depth):
  global arrive
  if depth == 5:
    arrive = True
    return
  visited[now] = True
  for i in A[now]:
    if not visited[i]:
      DFS(i, depth + 1) # 재귀 호출마다 깊이 증가
  visited[now] = False

# 탐색
for i in range(N):
  DFS(i, 1)
  if arrive:
    break

## 출력
if arrive:
  print(1)
else:
  print(0)