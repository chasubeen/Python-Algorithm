import sys
input = sys.stdin.readline

## 입력
mod = 1000000000
N = int(input())
D = [[0 for j in range(11)] for i in range(N+1)]

## 처리
for i in range(1, 10):
    D[1][i] = 1 # 길이가 1일 때 만드는 높이 h로 끝나는 계단 수의 모든 경우의 수는 1
                # 단, 0으로 시작하는 숫자는 없기 때문에 D[0][1]은 0으로 초기화

for i in range(2, N+1):
    D[i][0] = D[i-1][1] # N에서 높이가 0이면서 N-1에서는 높이가 1이여야 계단 수 가능
    D[i][9] = D[i-1][8] # N에서 높이가 9이면서 N-1에서는 높이가 8이어야 계단 수 가능
    for j in range(1, 9):
        # 높이가 1 ~ 8이면서 N-1에서 자신보다 한 단계 위 또는 한 단계 아래 높이에서 오는 것이 가능
        D[i][j] = (D[i-1][j-1] + D[i-1][j+1]) % mod 

sum = 0

for i in range(10):
    sum = (sum + D[N][i]) % mod # 정답 값을 더할 때도 mod 연산이 필요함

## 출력
print(sum)