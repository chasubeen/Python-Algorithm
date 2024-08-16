## 입력
N = int(input()) # 도시 수
M = int(input()) # 여행 계뢱에 속한 도시 수
# 도시 연결 데이터 리스트
dosi = [[0 for j in range(N+1)] for i in range(N+1)]

## 처리
# find 연산
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
# union 연산
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for i in range(1, N+1):
    # 도시 간 연결 데이터 저장
    dosi[i] = list(map(int, input().split())) 
    # 인덱스 1부터 시작이기에 0번째에 0 데이터 삽입 필요
    dosi[i].insert(0, 0)

# 여행 계획 도시 저장 리스트
route = list(map(int, input().split()))
route.insert(0, 0)

# 대표 노드 저장 리스트
parent = [0]*(N+1)

for i in range(1, N+1):
    # 대표 노드를 자기 자신으로 초기화
    parent[i] = i

# 인접 행렬 탐색
for i in range(1, N+1):
    for j in range(1, N+1):
        if dosi[i][j] == 1:
            union(i,j) # 도시가 연결되어 있는 경우 -> union 연산

# 여행 계획 도시들이 1개의 대표 도시로 연결돼 있는지 확인
# 이후 isConnect 값 저장
index = find(route[1])
isConnect = True
for i in range(2, len(route)):
    if index != find(route[i]):
        isConnect = False
        break

## 출력
if isConnect:
    print("YES")
else:
    print("NO")