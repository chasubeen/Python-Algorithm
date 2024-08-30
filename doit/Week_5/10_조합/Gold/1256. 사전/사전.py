import sys
input = sys.stdin.readline

## 입력
# a 문자 개수, z 문자 개수, k(순번)
N, M, K = map(int, input().split())
# 조합 경우의 수 저장 테이블
D = [[0 for j in range(202)] for i in range(202)] 


## 처리
# 조합 테이블 -> 미리 생성
for i in range(0, 201):
    # 고르는 수의 개수는 전체 개수를 넘을 수 없음
    for j in range(0, i + 1):
        if j == 0 or j == i:
            D[i][j] = 1
        else:
            D[i][j] = D[i - 1][j - 1] + D[i - 1][j]
            # K의 범위를 벗어나는 경우 최댓값 저장
            if D[i][j] > 1000000000:
                D[i][j] = 1000000001

# 모두 불가능인 경우
if D[N + M][M] < K:
    print(-1)
    
else:
    # 모든 문자를 사용할 때까지
    while not (N == 0 and M == 0):
        if D[N - 1 + M][M] >= K:
            print("a", end='')
            N -= 1
        else:
            print("z", end='')
            K -= D[N - 1 + M][M]
            M -= 1