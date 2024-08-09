## 입력
N, K = map(int, input().split()) # 동전 개수, 목표 금액
A = [0] * N
for i in range(N):
  A[i] = int(input())

## 처리
# 가치가 큰 동전부터 선택해야 개수를 최소로 구성할 수 있음
count = 0
for i in range(N-1, -1, -1):
  if A[i] <= K:
    count += K//A[i]
    K = K%A[i]

## 출력
print(count)