import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())  # 원소 개수, 질의 개수
parent = list(range(N + 1))  # 대표 노드 저장 리스트

# find 연산(대표 노드를 반환하는 과정)
def find(a):
    if a == parent[a]:
        return a
    # 재귀 형태로 구현 -> 경로 압축 부분
    parent[a] = find(parent[a])
    return parent[a]

# union 연산(하나의 집합으로 합치는 과정)
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

# 두 원소가 같은 집합인지 확인
def checkSame(a, b):
    return find(a) == find(b)

# 처리
for _ in range(M):
    question, a, b = map(int, input().split())

    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("YES")
        else:
            print("NO")
