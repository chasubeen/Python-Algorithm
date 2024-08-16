import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

## 입력
N = int(input()) # 테스트 케이스 개수
IsEven = True # 이분 그래프 판별 변수

## 처리
# DFS 구현
def DFS(v):
  global IsEven
  # 현재 노드 방문 기록하기
  visited[v] = True
  for i in A[v]:
    if not visited[i]:
      # 인접 노드는 같은 집합이 x
      # 다른 집합으로 처리
      check[i] = (check[v] + 1)%2
      DFS(i)

    # 이미 방문한 노드가 현재 내 노드와 같은 집합이면
    # 이분 그래프가 아님
    elif check[v] == check[i]:
      IsEven = False

for _ in range(N):
  V, E = map(int, input().split()) # node, edge
  A = [[] for _ in range(V+1)] # 그래프 데이터 저장 인접 리스트
  visited = [False] * (V+1) # 방문 기록 저장 리스트
  check = [0] * (V+1) # 방문 기록 저장 리스트
  IsEven = True # 이분 그래프 판별 변수(초기화)

  # 인접 리스트에 그래프 데이터 저장
  for i in range(E):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

  for i in range(1, V+1):
    # 각 노드에서 DFS 실행
    # 결과가 이분 그래프가 아니면 반복 종료
    if IsEven:
      DFS(i)
    else:
      break

  ## 출력
  # 이분 그래프 여부 출력
  if IsEven:
    print("YES")
  else:
    print("NO")