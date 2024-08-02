# 빠른 입출력
import sys
print = sys.stdout.write

## 입력
A = list(input())

## 처리
for i in range(len(A)):
  Max = i
  for j in range(i+1, len(A)):
    # 내림차순 정렬 -> 최댓값 탐색
    if A[j] > A[Max]:
      Max = j

  if A[i] < A[Max]:
    temp = A[i]
    A[i] = A[Max]
    A[Max] = temp

## 출력
for i in range(len(A)):
  print(A[i])