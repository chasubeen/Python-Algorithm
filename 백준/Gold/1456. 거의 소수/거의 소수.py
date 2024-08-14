import math

## 입력
Min, Max = map(int, input().split()) # 시작, 종료 수
A = [0] * (10000001) # 소수 리스트

## 처리
for i in range(2, len(A)):
  A[i] = i

# 제곱근까지만 수행
for j in range(2, int(math.sqrt(len(A))) + 1):
  # 이미 지워진 수라면 넘어감
  if A[j] == 0:
    continue
  
  # 소수의 배숫값 반복
  for k in range(2 * j, len(A), j):
    A[k] = 0

count = 0

for i in range(2, 10**7 + 1):
  if A[i] != 0:
    temp = A[i]

    # 변수의 표현 범위를 넘어갈 수 있기에 이항 정리로 처리
    while A[i] <= Max / temp:
      if A[i] >= Min/temp:
        count += 1
      temp = temp * A[i]
      
## 출력
print(count)