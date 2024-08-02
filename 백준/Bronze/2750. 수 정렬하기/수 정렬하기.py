## 입력
N = int(input())
A = [0] * N
for i in range(N):
  A[i] = int(input())

## 처리(정렬)
for i in range(N-1):
  # 정렬 완료 지점 설정
  for j in range(N-i-1):
    if A[j] > A[j+1]:
      temp = A[j]
      A[j] = A[j+1]
      A[j+1] = temp

## 출력
for i in range(N):
  print(A[i])