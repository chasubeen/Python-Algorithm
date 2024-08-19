import sys
from collections import deque
input = sys.stdin.readline

## 입력
N = int(input()) # 도시 개수
M = int(input()) # 도로 수
A = [[] for _ in range(N+1)] # 도시 인접 리스트
reverseA = [[] for _ in range(N+1)] # 역방향 인접 리스트
indegree = [0]*(N+1) # 진입 차수 리스트

# 인접 도시 정보 저장
for i in range(M):
    S, E, V = map(int, input().split())
    A[S].append((E, V))
    reverseA[E].append((S, V))  # 역방향 에지 정보 저장
    indegree[E] += 1    # 진입 차수 리스트 저장

# 시작 도시, 도착 도시
startDosi, endDosi = map(int, input().split())

## 처리(위상 정렬)
queue = deque() # 큐 생성
queue.append(startDosi) # 출발 도시 삽입
result = [0]*(N+1) # 결과

# 위상 정렬 수행
while queue:    
    now = queue.popleft() # 현재 노드
    # 현재 노드에서 갈 수 있는 노드 탐색
    for next in A[now]:
        indegree[next[0]] -= 1
        result[next[0]] = max(result[next[0]],result[now] + next[1])
        if indegree[next[0]] == 0:
            queue.append(next[0])

resultCount = 0 # 1분도 쉬지 않고 달려야 하는 도로의 수
visited = [False]*(N+1) # 도시 방문 유무

queue.clear() 
queue.append(endDosi) # 도착 도시를 큐에 삽입
visited[endDosi] = True

# 도착 도시에서 '역방향'으로 위상 정렬 수행
while queue:     
    now = queue.popleft()
    for next in reverseA[now]:
        # 1분도 쉬지 않는 도로 체크
        if result[next[0]] + next[1] == result[now]:
            resultCount += 1
            if not visited[next[0]]:
                visited[next[0]] = True
                queue.append(next[0])

## 출력
print(result[endDosi]) # 만나는 시간
print(resultCount) # 1분도 쉬지 않고 달려야 하는 도로의 수