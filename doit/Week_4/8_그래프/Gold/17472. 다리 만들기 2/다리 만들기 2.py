import copy
import sys
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline

## 입력
# 네 방향 탐색을 위한 상수
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 행렬의 크기
N, M = map(int, input().split())
# 맵 정보 저장 리스트
myMap = [[0 for j in range(M)] for i in range(N)]
# BFS 시 방문 여부 저장 리스트
visited = [[False for j in range(M)] for i in range(N)]

# 지도 정보 저장
for i in range(N):
    myMap[i] = list(map(int, input().split()))

# 섬 정보
sNum = 1 # 번호
sumlist = list([]) # 모든 정보 이중 리스트
mlist = [] # 1개 섬에 대한 정보

# 섬에 한 칸(노드)을 더해주는 함수
def addNode(i, j, queue):
    myMap[i][j] = sNum
    visited[i][j] = True
    temp = [i, j]
    mlist.append(temp) # 섬 정보에 해당 노드 추가
    queue.append(temp) # BFS를 위한 큐에 해당 노드 추가

# 탐색 -> 섬 정보 저장
def BFS(i, j):
    queue = deque()
    mlist.clear()
    start = [i, j] # 탐색 시작 위치
    queue.append(start)
    mlist.append(start)
    visited[i][j] = True
    myMap[i][j] = sNum
    
    # i,j 위치에서 네 방향으로 연결된 모든 노드를 탐색하여 
    # 1개 섬의 영역 확장
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            tempR = dr[d]
            tempC = dc[d]
            while r + tempR >= 0 and r + tempR < N and c + tempC >= 0 and c + tempC < M:
                if not visited[r + tempR][c + tempC] and myMap[r + tempR][c + tempC] != 0:
                    # 연결된 새로운 노드가 확인되면 addNode를 통해 정보 저장
                    addNode(r + tempR, c + tempC, queue);
                else:
                    break;
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1
    return mlist

# 섬 구분 작업 수행
for i in range(N):
    for j in range(M):
        if myMap[i][j] != 0 and not visited[i][j]:
            tempList = copy.deepcopy(BFS(i, j)) # 하나의 섬 정보 가져오기
                                                # 깊은 복사로 해주어야 주소를 공유하지 않음
            sNum += 1 # 새로운 섬 넘버링
            sumlist.append(tempList) # BFS 결과를 sumList에 추가

pq = PriorityQueue() # 우선순위 큐

# 모든 섬에서 지을 수 있는 다리를 찾고 저장
for now in sumlist: # 1개 섬 정보 추출
    for temp in now: 
        r = temp[0]
        c = temp[1]
        now_S = myMap[r][c]
        for d in range(4):
            tempR = dr[d]
            tempC = dc[d]
            blenght = 0
            # 1개의 섬의 모든 위치에서 만들 수 있는 다리 정보 저장
            while r + tempR >= 0 and r + tempR < N and c + tempC >= 0 and c + tempC < M:
                if myMap[r + tempR][c + tempC] == now_S:  # 같은 섬이면 에지를 만들 수 없음
                    break
                elif myMap[r + tempR][c + tempC] != 0:  # 같은 섬도 아니고 바다도 아니면
                    if blenght > 1:  # 다른 섬 → 길이가 1 이상일 때 에지로 더하기
                        pq.put((blenght, now_S, myMap[r + tempR][c + tempC]))
                    break
                else:  # 바다이면 다리의 길이 연장
                    blenght += 1
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1


## === 유니온 파인드 ===
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


parent = [0] * sNum # 대표 노드 저장 리스트
# 자기 자신을 대표 노드로 초기화
for i in range(len(parent)):
    parent[i] = i

useEdge = 0 # 사용한 에지의 수
result = 0 # 정답 변수

# 큐가 빌 때까지
while pq.qsize() > 0:
    v, s, e = pq.get()
    if find(s) != find(e): # 연결해도 사이클이 생기지 않으면
        union(s, e)
        result += v
        useEdge += 1

## 출력
if useEdge == sNum - 2: # sNum이 실제 섬의 수보다 1 크다.
    print(result)
else:
    print(-1)