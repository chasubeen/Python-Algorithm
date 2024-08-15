import math

## 입력
M, N = map(int, input().split()) # 시작, 종료
A = [0] * (N+1) # 소수 리스트

## 처리
# 각각의 인덱스 값으로 초기화
# 1은 소수가 아니니 애초에 0으로 처리해 둠
for i in range(2, N+1):
  A[i] = i

for i in range(2, int(math.sqrt(N) + 1)):
  # 이미 제거된 수 -> 넘어감
  if A[i] == 0:
    continue
  # 배수 지우기
  for j in range(2 * i, N+1, i):
    A[j] = 0
  
## 출력
for i in range(M, N+1):
  if A[i] != 0:
    print(i)