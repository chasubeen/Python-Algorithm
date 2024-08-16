## 입력(+ 변수 초기화)
N = int(input()) # 재료의 개수
A = [[] for _ in range(N)] # 인접 리스트
visited = [False] * (N) # DFS 탐색 시 탐색 여부 저장 리스트
D = [0] * N # 각 노드값 저장 리스트
lcm = 1 # 최소공배수

## 처리
# gcd 함수
def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a%b)

# 탐색 함수 구현
def DFS(v):
  visited[v] = True
  for i in A[v]:
    next = i[0]
    if not visited[next]:
      D[next] = D[v] * i[2] // i[1]
      DFS(next)
      
for i in range(N-1):
  a, b, p, q = map(int, input().split())
  A[a].append((b, p, q)) # a:b = p:q
  A[b].append((a, q, p)) # b:a = q:p
  lcm *= (p*q // gcd(p,q)) # 최소 공배수 = (두 수의 곱) / 최대공약수

D[0] = lcm
DFS(0)
mgcd = D[0] # 모든 node의 최대공약수

for i in range(1, N):
  mgcd = gcd(mgcd, D[i])

## 출력
for i in range(N):
  print(int(D[i] // mgcd), end = ' ')
