# 빠른 입출력
import sys
input = sys.stdin.readline

## 입력
N = int(input()) # 데이터 개수
A = []

for i in range(N):
  A.append( (int(input()), i) ) # (data, index) 튜플
## 처리
# 정렬
sorted_A = sorted(A)
Max = 0

for i in range(N):
  if Max < sorted_A[i][1] - i:
    Max = sorted_A[i][1] - i

## 출력
print(Max + 1)