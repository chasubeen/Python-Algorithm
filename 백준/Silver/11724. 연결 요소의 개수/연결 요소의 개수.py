import sys
sys.setrecursionlimit(10000) # 재귀 함수의 탐색 한도 증가
input = sys.stdin.readline

## 입력
n, m = map(int, input().split())
A = [[] for _ in range(n+1)] # 인접 리스트
                             # 이중 리스트 활용
visited = [False] * (n+1)

# DFS -> 재귀 함수 형태로 구현
def DFS(v):
  # 현재 방문한 노드의 방문 기록 작성
  visited[v] = True
  for i in A[v]:
    if not visited[i]:
      DFS(i)

## 처리
for _ in range(m):
  # 간선의 양 끝점 입력
  s,e = map(int, input().split())
  
  # 양방향 에지이므로 양쪽에 에지를 더하기
  A[s].append(e)
  A[e].append(s)

count = 0

for i in range(1, n+1):
  # 연결 노드 중 방문하지 않았던 노드만 탐색
  if not visited[i]:
    count += 1
    DFS(i)

## 출력
print(count)