import sys

## 입력
# 유저 수, 친구 관계 수
N, M = map(int, input().split())
# 데이터 저장을 위한 인접 행렬
distance = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]
for i in range(1, N+1): 
    distance[i][i] = 0 # 인접 행렬 초기화

## 처리
for i in range(M):
    # 친구 관계 데이터 저장
    s, e = map(int, input().split())
    # 양방향 에지로 저장, 가중치 = 1
    distance[s][e] = 1
    distance[e][s] = 1

# 플로이드 워셜 수행
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

## 출력
Min = sys.maxsize
Answer = -1

for i in range(1, N+1):
    temp = 0
    for j in range(1, N+1):
        temp += distance[i][j]
    # 가장 작은 케빈 베이컨의 수를 지닌 i 찾기
    if Min > temp:  
        Min = temp
        Answer = i

print(Answer)