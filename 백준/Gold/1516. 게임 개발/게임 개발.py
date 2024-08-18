from collections import deque

## 입력
N = int(input())
A = [[] for _ in range(N+1)] # 비교 데이터 저장 인접 리스트
indegree = [0] * (N+1) # 진입 차수 리스트
selfBuild = [0] * (N+1) # 자기 자신을 짓는 데 걸리는 시간 저장 리스트

## 처리
for i in range(1, N+1):
  # 인접 리스트 데이터 저장
  inputList = list(map(int, input().split())) 
  selfBuild[i] = (inputList[0]) # 건물을 짓는 데 걸리는 시간
  index = 1
  while True: # 인접 리스트 만들기
    preTemp = inputList[index] # 먼저 지어야 하는 건물
    index += 1
    # 먼저 지어야 하는 건물이 더 이상 없으면
    if preTemp == -1:
      break
    A[preTemp].append(i)
    indegree[i] += 1 # 진입 차수 데이터 저장

# 위상 정렬 수행
queue = deque()

for i in range(1, N+1):
  if indegree[i] == 0:
    queue.append(i)

result = [0] * (N+1) # 결과 저장 리스트

while queue:
  now = queue.popleft() # 현재 노드 가져오기
  for next in A[now]:
    indegree[next] -= 1
    # 시간 업데이트
    result[next] = max(result[next], result[now] + selfBuild[now])
    if indegree[next] == 0:
      queue.append(next)

## 출력
for i in range(1, N+1):
  print(result[i] + selfBuild[i])