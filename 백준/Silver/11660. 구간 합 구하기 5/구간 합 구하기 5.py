# 빠른 입출력을 위한 부분
import sys
input = sys.stdin.readline

## 입력
n, m = map(int, input().split())

## 처리
# 원본 리스트와 합 배열 만들기

A = [[0]*(n+1)] # 원본 리스트(1차원 배열로)
D = [[0] * (n+1) for _ in range(n+1)] # 합 배열(2차원 배열로)


# 원본 배열에 데이터 저장
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()] # row 처리
    A.append(A_row)

# 구간 합 구하기
for i in range(1, n+1):
    for j in range(1, n+1):
        # 합 배열 구하기
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

## 출력
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 구간 합 배열로 질의 답변
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)