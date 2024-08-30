import sys
input = sys.stdin.readline

## 입력
D = [[0 for j in range(31)] for i in range(31)] # DP 리스트

# DP 리스트 초기화
for i in range(0, 31):
    D[i][1] = i
    D[i][0] = 1
    D[i][i] = 1

## 처리 -> 점화식
for i in range(2, 31):
    for j in range(1, i):
        D[i][j] = D[i-1][j-1] + D[i-1][j] # 점화식

T = int(input()) # 질의 개수


## 출력
# D 테이블을 모두 구해 놓은 후 질의에 대한 답 출력
for i in range(0, T):
    N, M = map(int, input().split())
    print(D[M][N])