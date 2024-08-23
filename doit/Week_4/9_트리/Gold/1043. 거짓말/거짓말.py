## 입력

N, M = map(int, input().split()) # 사람 수, 파티 개수
trueP = list(map(int, input().split()))  # 진실을 아는 사람
T = trueP[0] # 진실을 아는 사람 수
del trueP[0] 
result = 0
party = [[] for _ in range(M)] # 파티 데이터

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
    # a와 b의 대표 노드 찾기
    a = find(a)
    b = find(b)

    # 두 원소의 대표 노드끼리 연결
    if a != b:
        parent[b] = a

# 두 원소가 같은 집합인지 확인
def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(M):
    # 파티 데이터 저장
    party[i] = list(map(int, input().split()))  
    del party[i][0]

parent = [0] * (N + 1)
for i in range(N + 1):  
    # 대표 노드를 자기 자신으로 초기화
    parent[i] = i

for i in range(M):  
    # 각 파티에 참여한 사람들을 1개의 그룹으로 만들기
    firstPeople = party[i][0]
    for j in range(1, len(party[i])):
        union(firstPeople, party[i][j])

#  각 파티의 대표 노드와 진실을 아는 사람들의 
# 대표 노드가 같다면 과장할 수 없음
for i in range(M):
    isPossible = True
    cur = party[i][0]
    for j in range(len(trueP)):
        if find(cur) == find(trueP[j]):
            isPossible = False
            break
    if isPossible:
        result += 1  # 모두 다르면 결괏값 1 증가

## 출력
print(result)