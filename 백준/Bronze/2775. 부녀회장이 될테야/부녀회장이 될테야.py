import sys
input = sys.stdin.readline

## 입력
D = [[0 for j in range(15)] for i in range(15)] # DP 리스트

# DP 리스트 초기화
for i in range(1, 15):
    D[i][1] = 1
    D[0][i] = i

## 처리 -> 점화식
for i in range(1, 15):
    for j in range(2, 15):
        D[i][j] = D[i][j-1] + D[i-1][j] # 점화식

T = int(input()) # 질의 개수


## 출력
# D 테이블을 모두 구해 놓은 후 질의에 대한 답 출력
for i in range(0, T):
    K = int(input())
    N = int(input())
    print(D[K][N])