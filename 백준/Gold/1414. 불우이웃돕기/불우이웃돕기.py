import sys
from queue import PriorityQueue
input = sys.stdin.readline

## 입력
N = int(input()) # 컴퓨터 개수
pq = PriorityQueue() # 랜선 정보를 저장할 우선순위 큐
sum = 0 # 모든 랜선 길이의 합

## 처리
for i in range(N):
    tempc = list(input()) # 한 줄씩 문자열 데이터 받기
    for j in range(N):
        temp = 0
        # 소문자일 때
        if 'a' <= tempc[j] <= 'z':
            temp = ord(tempc[j]) - ord('a') + 1
        # 대문자일 때
        elif 'A' <= tempc[j] <= 'Z':
            temp = ord(tempc[j]) - ord('A') + 27
          
        # sum에 현재 랜선 길이 더하기
        sum += temp
      
        # i와 j가 다르고 연결 랜선이 있다면
        if i != j and temp != 0:
            pq.put((temp, i, j)) # 랜선 정보 저장

# === Union Find ===
parent = [0] * N # 대표 노드 저장 리스트
for i in range(N):
    parent[i] = i # 자기 자신을 대표 노드로 초기화

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

# === MST 수행 ===
useEdge = 0 # 사용 에지 수
result = 0 # 최소 신장 트리

while pq.qsize() > 0:
    v, s, e = pq.get() # 에지 정보 가져오기
    # 연결해도 사이클이 생기지 않으면
    if find(s) != find(e):
        union(s, e) # 유니온 연산 수행
        result += v # 에지 가중치를 정답 변수에 더하기
        useEdge += 1 # 사용 에지 수 count

## 출력
# 탐색이 완료되면
if useEdge == N - 1:
    print(sum - result) # 결과 자체는 전체 - 최솟값임
else:
    print(-1)